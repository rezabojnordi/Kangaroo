from flask_restx import Resource
from apis.models import cache
from core.util.db_helper import db_helper_obj as db
from core.util.job_worker import job_queue_app as jq


from .user_project import resource


@resource.response(400, "Bad Request")
@resource.response(401, "Unauthorized")
@resource.response(404, "No user-project found!")
@resource.route("/<string:user_project_id>/cache")
@resource.param('user_project_id', 'The user-project ID')
class UserProjectCache(Resource):
    """Update the cache configuration of a specific user-project"""

    @resource.doc(
        operationId="updateUserProjectCacheConfig",
        description="Update the existing user-project cache configuration",
        responses={
            200: ("Success"),
        },
    )
    @resource.expect(cache.cache_model)
    def put(self, user_project_id):
        """Update a specific user-project cache config"""

        return 200
