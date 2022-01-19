from flask_restx import fields, reqparse, inputs
from . import models_namespace
from .ssl import ssl_model
from .service import (
    services_dict,
    services_model,
    service_name_list,
    service_status_list,
    STATUS,
    DICT_SRV_NAME_KEY,
    DICT_SRV_MODEL_KEY,
)
from .domain import domain_model, DOMAIN
from .tag import tag_model, TAG
from core.util.model_util import get_model_field_desc


# Model
USER_NAME = "user_name"
PROJECT_NAME = "project_name"
PROJECT_OVERALL_STATUS = "status"
HTTPS_ENABLED = "https_enabled"
SSL_CONTENT = "ssl_content"
QUOTA_SIZE = "quota_size"
DATABASE_PASSWORD = "db_password"
FILEMANAGER_PASSWORD = "fm_password"
WORDPRESS_PASSWORD = "wp_password"
CACHE_TIME = "cache_validity_time"
DETAIL = "detail"
SERVICE_KEY = "services"
# Database
DB_PROJECT_ID = "project_id"
DB_DOMAIN_HTTPS = "domain_https"
DB_WP_PASSWORD = "wordpress.password"
DB_DB_PASSWORD = "database.password"
DB_FM_PASSWORD = "filemanager.password"
DB_QUOTA_SIZE = "storage.quota_size"
DB_CACHE_TIME = "nginx.cache.cache_valid"


new_user_project_request_model = models_namespace.model(
    "User Project New Request",
    {
        USER_NAME: fields.String(
            required=True,
            description="Username who owns the project",
            example="reza",
            pattern="^[^\-]+$",
            attribute=lambda x: x[DB_PROJECT_ID].split('-')[0],
        ),
        PROJECT_NAME: fields.String(
            required=True,
            description="Project name",
            example="example",
            pattern="^[^\-]+$",
            attribute=lambda x: x[DB_PROJECT_ID].split("-")[1],
        ),
        DOMAIN: domain_model[DOMAIN],
        TAG: tag_model[TAG],
        HTTPS_ENABLED: fields.Boolean(
            required=False,
            description="Determines if project uses HTTPS",
            example=True,
            default=True,
            attribute=DB_DOMAIN_HTTPS,
        ),
        SSL_CONTENT: fields.Nested(
            ssl_model,
            allow_null=True,
            attribute=lambda x: x,
        ),
        WORDPRESS_PASSWORD: fields.String(
            required=False,
            description="Wordpress dashboard login password",
            example="$3kur3",
            attribute=DB_WP_PASSWORD,
        ),
        QUOTA_SIZE: fields.Integer(
            required=False,
            description="Maximum volume size in GB",
            example=10,
            min=1,
            max=20,
            attribute=DB_QUOTA_SIZE,
        ),
        CACHE_TIME: fields.Integer(
            required=False,
            description="Maximum time of cached data being valid in hour",
            example=24,
            min=0,
            default=48,
            attribute=DB_CACHE_TIME,
        ),
    },
)

user_project_details_model = models_namespace.model(
    "User Project Detail",
    {
        SERVICE_KEY: fields.Nested(
            services_model,
            attribute=lambda x:x,
        ),
    },
)

user_project_response_model = models_namespace.inherit(
    "User Project Response",
    new_user_project_request_model,
    {
        DATABASE_PASSWORD: fields.String(
            required=False,
            description="Project Wordpress DB's password",
            example="$3kur3",
            attribute=DB_DB_PASSWORD,
        ),
        FILEMANAGER_PASSWORD: fields.String(
            required=False,
            description="File-manager login password",
            example="$3kur3",
            attribute=DB_FM_PASSWORD,
        ),
        PROJECT_OVERALL_STATUS: fields.String(
            required=True,
            description="User-project overall status",
            example="ready",
            attribute=PROJECT_OVERALL_STATUS,
        ),
        DETAIL: fields.Nested(
            user_project_details_model,
            attribute=lambda x:x,
        ),
    },
)

user_project_query_parser = reqparse.RequestParser()
user_project_query_parser.add_argument(
    reqparse.Argument(
        USER_NAME,
        store_missing=False,
        help=get_model_field_desc(new_user_project_request_model, USER_NAME),
    ),
)
user_project_query_parser.add_argument(
    reqparse.Argument(
        PROJECT_NAME,
        store_missing=False,
        help=get_model_field_desc(new_user_project_request_model, PROJECT_NAME),
    )
)
user_project_query_parser.add_argument(
    reqparse.Argument(
        DOMAIN,
        store_missing=False,
        help=get_model_field_desc(new_user_project_request_model, DOMAIN),
    )
)
user_project_query_parser.add_argument(
    reqparse.Argument(
        TAG,
        store_missing=False,
        help=get_model_field_desc(new_user_project_request_model, TAG),
    )
)
user_project_query_parser.add_argument(
    reqparse.Argument(
        PROJECT_OVERALL_STATUS,
        store_missing=False,
        help=get_model_field_desc(user_project_response_model, PROJECT_OVERALL_STATUS),
    )
)
user_project_query_parser.add_argument(
    reqparse.Argument(
        HTTPS_ENABLED,
        store_missing=False,
        type=inputs.boolean,
        help=get_model_field_desc(new_user_project_request_model, HTTPS_ENABLED),
    )
)
user_project_query_parser.add_argument(
    reqparse.Argument(
        QUOTA_SIZE,
        store_missing=False,
        help=get_model_field_desc(new_user_project_request_model, QUOTA_SIZE),
        type=int,
    )
)
for s in service_name_list:
    help_msg = services_dict[s][DICT_SRV_NAME_KEY]
    help_msg += " " + get_model_field_desc (services_dict[s][DICT_SRV_MODEL_KEY], STATUS)
    help_msg += f" (Can be one of {service_status_list})"

    user_project_query_parser.add_argument(
        reqparse.Argument(
            f"{s}_{STATUS}",
            store_missing=False,
            help=help_msg
        )
    )
