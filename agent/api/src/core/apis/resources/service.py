from flask_restx import Resource
from apis.models import service
from core.util.db_helper import db_helper_obj as db
from core.util.job_worker import job_queue_app as jq


from .user_project import resource


# Note that the word `service` for the user of API-Server is the same as the `job` word
# It's just prettier and more meaningful for the user!
@resource.response(400, "Bad Request")
@resource.response(401, "Unauthorized")
@resource.response(404, "No user-project found!")
@resource.route("/<string:user_project_id>/service")
@resource.param('user_project_id', 'The user-project ID')
class UserProjectServices(Resource):
    """Send a 'continue service process' request for a specific user-project"""

    @resource.doc(
        operationId="continueUserProjectContinueService",
        description="Continue the existing user-project's service",
        responses={
            200: ("Success"),
        },
    )
    @resource.expect(service.service_name_model)
    def post(self, user_project_id):
        """Continue a specific user-project's service"""
        data = resource.payload
        result = db.find_one_params({"project_id": user_project_id})
        if result == None:
            return 404
        username = result['project_id'].split('-')[0]
        project_name = result['project_id'].split('-')[1]
        db_password = result['database']['password']
        wp_password = result['wordpress']['password']
        domain_name = result['domain_name']
        if data['service'] == 'database':
            database_obj = {
                "tags": ['update-cluster'],
                "user_name": username,
                "project_name": project_name,
                "user_password": db_password,
                "project_sql_import": True
            }
            jq.signature('database', args=[str(result['_id']), database_obj]).set(queue="database").apply_async()
        elif data['service'] == 'wordpress':
            wordpress_obj = {
                "tags": ['update-cluster'],
                "user_name": username,
                "project_name": project_name,
                "user_password": wp_password,
                "domain_name": domain_name,
                "project_wordpress_import": True
            }
            jq.signature('wordpress', args=[str(result['_id']), wordpress_obj]).set(queue="wordpress").apply_async()
        else:
            return 400
        return 200
