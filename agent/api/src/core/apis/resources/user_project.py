from flask_restx import Namespace, Resource, marshal
from flask_restx._http import HTTPStatus
from apis.models import user_project, domain, ssl
from core.util.db_helper import db_helper_obj as db
from core.util.job_worker import job_chain as jc, job_queue_app as jq
from core.util.model_util import (
    create_user_project_query_object_by_args,
    convert_user_name_and_project_name_to_project_id,
)

resource = Namespace(
    name="User Project",
    path="/user-project",
    description="User Project related operations",
)


@resource.response(HTTPStatus.BAD_REQUEST, "Bad Request")
@resource.response(HTTPStatus.UNAUTHORIZED, "Unauthorized")
@resource.route("/")
class AllUserProjects(Resource):
    """
    Return all user-projects or create a new user-project. It's possible to
    filter the fetched result by sending query string parameters mentioned.
    """

    @resource.doc("getUserProjects")
    @resource.doc(
        description="Return [all|filtered] existing user-projects along with their information"
    )
    @resource.expect(user_project.user_project_query_parser)
    @resource.response(
        HTTPStatus.OK, "Success", [user_project.user_project_response_model]
    )
    @resource.response(HTTPStatus.NOT_FOUND, "No user-projects exist!")
    def get(self):
        """
        Return [all|filtered] user-projects
        """
        args = user_project.user_project_query_parser.parse_args()
        queryObject = create_user_project_query_object_by_args(args)
        results = db.find_many_params(queryObject)
        if results == []:
            return None, HTTPStatus.NOT_FOUND
        return marshal(results, user_project.user_project_response_model), HTTPStatus.OK

    @resource.doc("createUserProject")
    @resource.doc(description="Create a new user-project with the given configuration")
    @resource.expect(user_project.new_user_project_request_model)
    @resource.response(
        HTTPStatus.CREATED,
        "Successfully created",
        user_project.user_project_response_model,
    )
    @resource.response(
        HTTPStatus.CONFLICT, "A user-project with the same name already exists"
    )
    def post(self):
        """
        Create a new user-project
        """
        import string, secrets
        from random import randrange

        data = resource.payload
        letter_list = string.ascii_letters + string.digits + "_/#()!`$="
        fileManagerPass = "".join(
            secrets.choice(letter_list) for i in range(randrange(15, 20))
        )
        databasePass = "".join(
            secrets.choice(letter_list) for i in range(randrange(15, 20))
        )
        if (
            not user_project.WORDPRESS_PASSWORD in data
            or not data[user_project.WORDPRESS_PASSWORD]
        ):
            wordpressLoginPass = "".join(
                secrets.choice(letter_list) for i in range(randrange(15, 20))
            )
        else:
            wordpressLoginPass = data[user_project.WORDPRESS_PASSWORD]

        project_id = convert_user_name_and_project_name_to_project_id(
            data["user_name"], data["project_name"]
        )
        # TODO: Find a way to convert the model schema to DB data schema.
        # NOTE: There is already a way to convert in reverse.
        if db.find_one_params({user_project.DB_PROJECT_ID: project_id}):
            return None, HTTPStatus.CONFLICT
        user_project_db_obj = {
            user_project.DB_PROJECT_ID: project_id,
            domain.DB_DOMAIN: data[domain.DOMAIN],
            user_project.DB_DOMAIN_HTTPS: data[user_project.HTTPS_ENABLED],
            user_project.PROJECT_OVERALL_STATUS: "pending",
            "tag": data[user_project.TAG],
            "storage": {
                "status": "pending",
                "quota_size": data[user_project.QUOTA_SIZE],
            },
            "filemanager": {
                "status": "pending",
                "password": fileManagerPass,
            },
            "database": {
                "status": "pending",
                "password": databasePass,
                "project_sql_import": False,
            },
            "wordpress": {
                "status": "pending",
                "password": wordpressLoginPass,
                "project_wordpress_import": False,
            },
            "nginx": {
                "status": "pending",
                "cache": {
                    "cache_valid": data[user_project.CACHE_TIME],
                },
                "certificate": {
                    "pub": data[user_project.SSL_CONTENT][ssl.SSL_CONTENT_PUB],
                    "priv": data[user_project.SSL_CONTENT][ssl.SSL_CONTENT_PRIV],
                },
            },
        }
        # id = db.insert_one(user_project_db_obj)

        storage_obj = {
            "tags": ["init-cluster"],
            "user_name": data["user_name"],
            "project_name": data["project_name"],
            "quota_size": f"{data['quota_size']}GB",
        }
        filemanager_obj = {
            "tags": ["init-cluster"],
            "user_name": data["user_name"],
            "project_name": data["project_name"],
            "user_password": fileManagerPass,
            "project_name_dump": False,
        }
        database_obj = {
            "tags": ["init-cluster"],
            "user_name": data["user_name"],
            "project_name": data["project_name"],
            "user_password": databasePass,
            "project_sql_import": False,
        }
        wordpress_obj = {
            "tags": ["init-cluster"],
            "user_name": data["user_name"],
            "project_name": data["project_name"],
            "user_password": wordpressLoginPass,
            "domain_name": data[domain.DOMAIN],
            "project_wordpress_import": False,
        }
        nginx_obj = {
            "tags": ["init-cluster"],
            "user_name": data["user_name"],
            "project_name": data["project_name"],
            # "user_password": data['project_password'],
            "domain_name": data[domain.DOMAIN],
            "cache_valid": data[user_project.CACHE_TIME],
            "domain_https": False,
            "fullchain": data[user_project.SSL_CONTENT][ssl.SSL_CONTENT_PUB],
            "privkey": data[user_project.SSL_CONTENT][ssl.SSL_CONTENT_PRIV],
        }
        # jc(
        #     jq.signature("storage", args=[str(id), storage_obj]).set(
        #         queue="storage"),
        #     jq.signature("filemanager", args=[filemanager_obj]).set(
        #         queue="filemanager"),
        #     jq.signature("database", args=[database_obj]).set(
        #         queue="database"),
        #     jq.signature("wordpress", args=[wordpress_obj]).set(
        #         queue="wordpress"),
        #     jq.signature("nginx", args=[nginx_obj]).set(queue="nginx")
        # ).apply_async()
        return (
            marshal(user_project_db_obj, user_project.user_project_response_model),
            HTTPStatus.CREATED,
        )


@resource.response(400, "Bad Request")
@resource.response(401, "Unauthorized")
@resource.response(404, "No user-project found!")
@resource.route("/<string:user_project_id>")
@resource.param("user_project_id", "The user-project ID")
class SingleUserProject(Resource):
    """
    Return the current configuration of a specific user-project or delete it
    """

    @resource.doc(
        operationId="getUserProjectInfo",
        description="Return the existing user-project along with its information",
        responses={
            200: ("Success", user_project.user_project_response_model),
        },
    )
    def get(self, user_project_id):
        """Return a specific user-project"""
        result = db.find_one_params({"project_id": user_project_id})
        if result == None:
            return 404
        result.pop("_id", None)
        pid = result.pop("project_id", None).split("-")
        result["user_name"] = pid[0]
        result["project_name"] = pid[1]
        # up = {}
        # up['user_name'] = result['project_id'].split('-')[0]
        # up['project_name'] = result['project_id'].split('-')[1]
        # up['project_password'] = result['database']['password']
        # up['quota_size'] = result['storage']['quota_size']
        # up['domain_name'] = result['domain_name']
        # up['domain_https'] = result['domain_https']
        # up['project_wordpress_import'] = result['wordpress']['project_wordpress_import']
        # up['project_sql_import'] = result['database']['project_sql_import']
        # up['cache_valid'] = result['nginx']['cache']['cache_valid']
        # up['pub'] = result['nginx']['certificate']['pub']
        # up['priv'] = result['nginx']['certificate']['priv']
        # up['tag'] = result['tag']
        return result, 200

    @resource.doc(
        operationId="deleteUserProject",
        description="Delete the entire specific user-project",
        responses={
            202: ("Success"),
        },
    )
    def delete(self, user_project_id):
        """Delete a specific user-project"""
        result = db.find_one_params({"project_id": user_project_id})
        if result == None:
            return 404
        db.update_one({"project_id": user_project_id}, {"status": "deleting"})
        user_name = result["project_id"].split("-")[0]
        project_name = result["project_id"].split("-")[1]
        obj = {
            "tags": ["remove-cluster"],
            "user_name": user_name,
            "project_name": project_name,
        }
        jc(
            jq.signature("nginx", args=[str(result["_id"]), obj]).set(queue="nginx"),
            jq.signature("wordpress", args=[obj]).set(queue="wordpress"),
            jq.signature("database", args=[obj]).set(queue="database"),
            jq.signature("filemanager", args=[obj]).set(queue="filemanager"),
            jq.signature("storage", args=[obj]).set(queue="storage"),
        ).apply_async()
        return None, 202
