# TODO: from apis.models.user_project import (


USER_PROJECT_ID = "project_id"


def get_model_field_desc(model, field_name):
    try:
        return model[field_name].__dict__["description"]
    except:
        return ""


def convert_user_project_id_to_user_and_project(project_id):
    try:
        [user_name, project_name] = project_id.split("-")
        return [user_name, project_name]
    except:
        return [None, None]


def convert_user_name_and_project_name_to_project_id(user_name, project_name):
    if "-" in user_name or "-" in user_name:
        return None
    return f"{user_name}-{project_name}"


def remove_object_id_key(db_obj):
    if isinstance(db_obj, list):
        for obj in db_obj:
            obj.pop("_id", None)
    else:
        db_obj.pop("_id", None)


def create_user_project_query_object_by_args(args):
    from apis.models.user_project import (
        USER_NAME,
        PROJECT_NAME,
        HTTPS_ENABLED,
        QUOTA_SIZE,
        DB_DOMAIN_HTTPS,
    )
    from apis.models.service import STATUS, service_name_list
    # TODO: Do better idea for this!
    STORAGE_KEY = service_name_list[0]

    # TODO: Clean this mess, really!
    # To become more readable it needs to have a well defined &
    # an interchangable structure for stored data in components
    # like `Database`, `Ansible`, so on.

    queryObject = {}
    try:
        for arg in args:
            val = args.get(arg)
            if val != None:
                if arg == USER_NAME or arg == PROJECT_NAME:
                    if not USER_PROJECT_ID in queryObject:
                        queryObject[USER_PROJECT_ID] = "-"
                    if arg == USER_NAME:
                        queryObject[USER_PROJECT_ID] = (
                            val + queryObject[USER_PROJECT_ID]
                        )
                    elif arg == PROJECT_NAME:
                        queryObject[USER_PROJECT_ID] = (
                            queryObject[USER_PROJECT_ID] + val
                        )
                elif arg == HTTPS_ENABLED:
                    queryObject[DB_DOMAIN_HTTPS] = val
                elif arg == QUOTA_SIZE:
                    if arg == QUOTA_SIZE:
                        queryObject[f"{STORAGE_KEY}.{QUOTA_SIZE}"] = val
                elif f"_{STATUS}" in arg:
                    queryObject[arg.replace("_", ".")] = val
                else:
                    queryObject[arg] = val
        if USER_PROJECT_ID in queryObject:
            if queryObject[USER_PROJECT_ID].startswith("-"):
                queryObject[USER_PROJECT_ID] = {
                    "$regex": f"{queryObject[USER_PROJECT_ID]}$"
                }
            if queryObject[USER_PROJECT_ID].endswith("-"):
                queryObject[USER_PROJECT_ID] = {
                    "$regex": f"^{queryObject[USER_PROJECT_ID]}"
                }
        return queryObject
    except:
        return {}


# def convert_db_schema_to_model(db_obj):
#     model_obj = {}
#     [
#         model_obj[USER_NAME],
#         model_obj[PROJECT_NAME],
#     ] = convert_user_project_id_to_user_and_project(db_obj[USER_PROJECT_ID])

#     return model_obj
