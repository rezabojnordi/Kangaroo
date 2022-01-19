from flask_restx import Resource
from core.util.db_helper import db_helper_obj as db
from core.util.job_worker import job_queue_app as jq


from .user_project import resource


@resource.response(400, "Bad Request")
@resource.response(401, "Unauthorized")
@resource.response(404, "No user-project found!")
@resource.route("/<string:user_project_id>/monitoring/visit")
@resource.param('user_project_id', 'The user-project ID')
class UserProjectMonitoringVisit(Resource):
    """Return the count of a specific user-project's clients visits"""

    @resource.doc(
        operationId="getUserProjectVisit",
        description="Return the user's client visit count in specific time period of the specific user-project",
        responses={
            200: ("Success"),
        },
    )
    def get(self, user_project_id):
        """Return a user-project's clients visit"""

        return 200


@resource.response(400, "Bad Request")
@resource.response(401, "Unauthorized")
@resource.response(404, "No user-project found!")
@resource.route("/<string:user_project_id>/monitoring/cache")
@resource.param('user_project_id', 'The user-project ID')
class UserProjectMonitoringCache(Resource):
    """Return the total cached data size of a specific user-project"""

    @resource.doc(
        operationId="getUserProjectCacheSize",
        description="Return the total cached data size of the specific project",
        responses={
            200: ("Success"),
        },
    )
    def get(self, user_project_id):
        """Return a user-project's cached data size"""

        return 200


@resource.response(400, "Bad Request")
@resource.response(401, "Unauthorized")
@resource.response(404, "No user-project found!")
@resource.route("/<string:user_project_id>/monitoring/resource")
@resource.param('user_project_id', 'The user-project ID')
class UserProjectMonitoringResource(Resource):
    """Return the current resource usage of the specific user-project"""

    @resource.doc(
        operationId="getUserProjectResourceUsage",
        description="Return the current resource usage of the specific user-project",
        responses={
            200: ("Success"),
        },
    )
    def get(self, user_project_id):
        """Return a user-project's resource usage"""

        return 200
