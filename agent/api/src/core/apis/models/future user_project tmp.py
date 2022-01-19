from flask_restx import fields
from . import models_namespace


# __all__ = ()


USER_NAME = "user_name"
PROJECT_NAME = "project_name"
TAG = "tag"
HTTPS_ENABLED = "https_enabled"
SSL_CONTENT = "ssl"
DOMAIN_NAME = "domain_name"
DATABASE_PASSWORD = "db_password"
FILEMANAGER_PASSWORD = "fm_password"
WORDPRESS_PASSWORD = "wp_password"
CACHE_TIME = "cache_time"
STORAGE_SIZE = "storage_size"
PROJECT_OVERALL_STATUS = "status"
# Detailed:

test = {
    USER_NAME: fields.String(),
    PROJECT_NAME: "project_name",
    TAG: "tag",
    HTTPS_ENABLED: "https_enabled",
    SSL_CONTENT: "ssl",
    DOMAIN_NAME: "domain_name",
    DATABASE_PASSWORD: "db_password",
    FILEMANAGER_PASSWORD: "fm_password",
    WORDPRESS_PASSWORD: "wp_password",
    CACHE_TIME: "cache_time",
    STORAGE_SIZE: "storage_size",
    PROJECT_OVERALL_STATUS: "status",
}

userProjectModel = models_namespace.model("User Project", {
    USER_NAME: fields.Raw(),
    PROJECT_NAME: fields.Raw(),
    TAG: fields.Raw(),
    HTTPS_ENABLED: fields.Raw(),
    SSL_CONTENT: fields.Raw(),
    DOMAIN_NAME: fields.Raw(),
    DATABASE_PASSWORD: fields.Raw(),
    FILEMANAGER_PASSWORD: fields.Raw(),
    WORDPRESS_PASSWORD: fields.Raw(),
    CACHE_TIME: fields.Raw(),
    STORAGE_SIZE: fields.Raw(),
    PROJECT_OVERALL_STATUS: fields.Raw(),
})

detailedUserProjectModel = models_namespace.inherit("Detailed User Project", userProjectModel, {
    "status": fields.Integer(),
})

"""
userProjectModel = models_namespace.model("User Project", {
    "user_name":
        fields.String(required=True,
                      description="Username who owns the project",
                      example="reza",
                      pattern="^[^\-]+$"),
    "project_name":
        fields.String(required=True,
                      description="Project name",
                      example="example",
                      pattern="^[^\-]+$"),
    "project_password":
        fields.String(required=True,
                      description="Project DB password",
                      example="$3kur3"),
    "quota_size":
        fields.Integer(required=False,
                       description="Maximum volume size in GB",
                       example=10,
                       min=1,
                       max=20),
    "domain_name":
        fields.String(required=True,
                      description="Project domain address",
                      example="example.com",
                      pattern="^(((?!-))(xn--|_{1,1})?[a-z0-9-]{0,61}[a-z0-9]{1,1}\.)*(xn--)?([a-z0-9][a-z0-9\-]{0,60}|[a-z0-9-]{1,30}\.[a-z]{2,})$"),
    "domain_https":
        fields.Boolean(required=False,
                       description="Determines if project uses HTTPS",
                       example=True,
                       default=True),
    "project_wordpress_import":
        fields.Boolean(required=False,
                       description="Determines if project starts up by using existing Wordpress filesystem backup",
                       example=False,
                       default=False),
    "project_sql_import":
        fields.Boolean(required=False,
                       description="Determines if project starts up by using existing Wordpress DB backup",
                       example=False,
                       default=False),
    "cache_valid":
        fields.Integer(required=False,
                       description="Maximum time of cached data being valid in hour",
                       example=24,
                       min=0,
                       default=48),
    "pub":
        fields.String(required=True,
                      description="SSL full chain file content"),
    "priv":
        fields.String(required=True,
                      description="SSL private chain file content"),
    # WUI Backend will control the tag values, and we don't
    "tag":
        fields.String(required=False,
                      description="Optional user-project tag content",
                      example="verified"),
})
"""

class UserProjectModel():
    """
    """

    # Attributes
    _id = None
    userName = None
    projectName = None
    domain = {

    }
    domainName = None
    database = {}

    def update():
        # print (vars(self))
        pass

# UserProjectModel.update()