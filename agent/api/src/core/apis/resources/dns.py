from flask_restx import Resource
from apis.models import dns
from core.util.db_helper import db_helper_obj as db
from core.util.job_worker import job_queue_app as jq


from .user_project import resource


@resource.response(400, "Bad Request")
@resource.response(401, "Unauthorized")
@resource.response(404, "No user-project found!")
@resource.route("/<string:user_project_id>/dns")
@resource.param('user_project_id', 'The user-project ID')
class UserProjectDns(Resource):
    """Set the DNS configuration of a specific user-project"""

    @resource.doc(
        operationId="setUserProjectDns",
        description="Set the existing user-project DNS configuration",
        responses={
            200: ("Success"),
        },
    )
    @resource.expect(dns.dns_model)
    def post(self, user_project_id):
        """Set a specific user-project DNS config"""

        return 200
