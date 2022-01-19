from flask_restx import fields
from . import models_namespace
from .ssl import sslModel


# __all__ = ()


USER_NAME = "user_name"
PROJECT_NAME = "project_name"
DOMAIN_NAME = "domain_name"
TAG = "tag"
PROJECT_OVERALL_STATUS = "status"
HTTPS_ENABLED = "https_enabled"
SSL_CONTENT = "ssl_content"
STORAGE_SIZE = "storage_size"
DATABASE_PASSWORD = "db_password"
FILEMANAGER_PASSWORD = "fm_password"
WORDPRESS_PASSWORD = "wp_password"
CACHE_TIME = "cache_time"
# Detailed:


newUserProjectRequestModel = models_namespace.model("New User Project Request",
    {
        USER_NAME: fields.String(
            required=True,
            description="Username who owns the project",
            example="reza",
            pattern="^[^\-]+$",
        ),
        PROJECT_NAME: fields.String(
            required=True,
            description="Project name",
            example="example",
            pattern="^[^\-]+$",
        ),
        DOMAIN_NAME: fields.String(
            required=True,
            description="Project domain address",
            example="example.com",
            pattern="^(((?!-))(xn--|_{1,1})?[a-z0-9-]{0,61}[a-z0-9]{1,1}\.)*(xn--)?([a-z0-9][a-z0-9\-]{0,60}|[a-z0-9-]{1,30}\.[a-z]{2,})$",
        ),
        # WUI Backend will control the tag values and we don't
        TAG: fields.String(
            required=False,
            description="Optional user-project tag content",
            example="verified",
        ),
        HTTPS_ENABLED: fields.Boolean(
            required=False,
            description="Determines if project uses HTTPS",
            example=True,
            default=True,
        ),
        SSL_CONTENT: fields.Nested(
            sslModel,
            allow_null=True
        ),
        STORAGE_SIZE: fields.Integer(
            required=False,
            description="Maximum volume size in GB",
            example=10,
            min=1,
            max=20,
        ),
        DATABASE_PASSWORD: fields.String(
            required=False,
            description="Project DB's password",
            example="$3kur3"
        ),
        FILEMANAGER_PASSWORD: fields.String(
            required=False,
            description="File-manager login password",
            example="$3kur3"
        ),
        WORDPRESS_PASSWORD: fields.String(
            required=False,
            description="Wordpress dashboard login password",
            example="$3kur3"
        ),
        CACHE_TIME: fields.Integer(
            required=False,
            description="Maximum time of cached data being valid in hour",
            example=24,
            min=0,
            default=48,
        ),
    },
)
