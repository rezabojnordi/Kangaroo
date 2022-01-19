from flask_restx import Resource
from apis.models import ssl
from core.util.db_helper import db_helper_obj as db
from core.util.job_worker import job_queue_app as jq


from .user_project import resource


@resource.response(400, "Bad Request")
@resource.response(401, "Unauthorized")
@resource.response(404, "No user-project found!")
@resource.route("/<string:user_project_id>/ssl")
@resource.param('user_project_id', 'The user-project ID')
class UserProjectSsl(Resource):
    """Set the (new) SSL certification"""

    @resource.doc(
        operationId="setUserProjectSsl",
        description="Set the existing user-project SSL certification",
        responses={
            200: ("Success"),
        },
    )
    @resource.expect(ssl.ssl_model)
    def post(self, user_project_id):
        """Set a specific user-project SSL certification"""

        return 200
