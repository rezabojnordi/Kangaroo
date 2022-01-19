from flask_restx import Resource
from apis.models import tag
from core.util.db_helper import db_helper_obj as db


from .user_project import resource


@resource.response(400, "Bad Request")
@resource.response(401, "Unauthorized")
@resource.response(404, "No user-project found!")
@resource.route("/<string:user_project_id>/tag")
@resource.param('user_project_id', 'The user-project ID')
class UserProjectTag(Resource):
    """Change the tag value of a specific user-project"""

    @resource.doc(
        operationId="updateUserProjectTag",
        description="Update the existing user-project tag value",
        responses={
            200: ("Success"),
        },
    )
    @resource.expect(tag.tag_model)
    def put(self, user_project_id):
        """Update a specific user-project tag"""

        data = resource.payload
        tag_obj = {'tag': data['value']}
        query_obj = {'project_id': user_project_id}
        result = db.update_one(query_obj, tag_obj)
        if result == []:
            return 404
        return 200
