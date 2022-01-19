from flask_restx import Resource
from core.util.db_helper import db_helper_obj as db
from core.util.job_worker import job_queue_app as jq


from .user_project import resource


@resource.response(400, "Bad Request")
@resource.response(401, "Unauthorized")
@resource.response(404, "No user-project found!")
@resource.route("/<string:user_project_id>/backup/database")
@resource.param('user_project_id', 'The user-project ID')
class UserProjectDatabaseBackup(Resource):
    """Return the database backup process status or start it for a specific user-project"""

    @resource.doc(
        operationId="getUserProjectDatabaseBackupStatus",
        description="Return the existing user-project database backup process status",
        responses={
            200: ("Success"),
        },
    )
    def get(self, user_project_id):
        """Return a user-project's database backup status"""

        return 200

    @resource.doc(
        operationId="userProjectDatabaseBackup",
        description="Start the existing user-project database backup process",
        responses={
            200: ("Success"),
        },
    )
    def post(self, user_project_id):
        """Start a specific user-project database backup process"""

        return 200
