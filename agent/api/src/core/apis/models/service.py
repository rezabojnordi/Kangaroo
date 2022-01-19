from flask_restx import fields
from . import models_namespace
from .ssl import ssl_model
from .cache import cache_model
import random


service_status_list = ["pending", "processing", "failed", "ready"]
service_name_list = ["storage", "filemanager", "database", "wordpress", "nginx"]


DICT_SRV_NAME_KEY = "name"
DICT_SRV_MODEL_KEY = "model"
# Model
STATUS = "status"
MESSAGE = "message"
PASSWORD = "password"
CACHE_KEY = "cache"
WP_IMPORT = "project_wordpress_import"
SQL_IMPORT = "project_sql_import"
QUOTA_SIZE = "quota_size"
SSL_CERT_KEY = "certificate"
# Database
DB_STATUS = STATUS
DB_MESSAGE = MESSAGE
DB_PASSWORD = PASSWORD
DB_STORAGE_STATUS = f"{service_name_list[0]}.{DB_STATUS}"
DB_STORAGE_MESSAGE = f"{service_name_list[0]}.{DB_MESSAGE}"
DB_STORAGE_QUOTA_SIZE = f"{service_name_list[0]}.{QUOTA_SIZE}"
DB_FILEMANAGER_STATUS = f"{service_name_list[1]}.{DB_STATUS}"
DB_FILEMANAGER_MESSAGE = f"{service_name_list[1]}.{DB_MESSAGE}"
DB_FILEMANAGER_PASSWORD = f"{service_name_list[1]}.{DB_PASSWORD}"
DB_DATABASE_STATUS = f"{service_name_list[2]}.{DB_STATUS}"
DB_DATABASE_MESSAGE = f"{service_name_list[2]}.{DB_MESSAGE}"
DB_DATABASE_PASSWORD = f"{service_name_list[2]}.{DB_PASSWORD}"
DB_DATABASE_SQL_IMPORT = f"{service_name_list[2]}.{SQL_IMPORT}"
DB_WORDPRESS_STATUS = f"{service_name_list[3]}.{DB_STATUS}"
DB_WORDPRESS_MESSAGE = f"{service_name_list[3]}.{DB_MESSAGE}"
DB_WORDPRESS_PASSWORD = f"{service_name_list[3]}.{DB_PASSWORD}"
DB_WORDPRESS_SQL_IMPORT = f"{service_name_list[3]}.{WP_IMPORT}"
DB_NGINX_STATUS = f"{service_name_list[4]}.{DB_STATUS}"
DB_NGINX_MESSAGE = f"{service_name_list[4]}.{DB_MESSAGE}"


services_dict = {s: {DICT_SRV_NAME_KEY: s.title()} for s in service_name_list}


service_storage_model = models_namespace.model(
    f"Service {services_dict['storage'][DICT_SRV_NAME_KEY]}",
    {
        STATUS: fields.String(
            required=False,
            description="Service Status",
            enum=service_status_list,
            example=random.choice(service_status_list),
            attribute=DB_STORAGE_STATUS,
        ),
        MESSAGE: fields.String(
            required=False,
            description="Last action message",
            example="No such file or directory!",
            attribute=DB_STORAGE_MESSAGE,
        ),
        QUOTA_SIZE: fields.Integer(
            required=False,
            description="Maximum volume size in GB",
            example=10,
            min=1,
            max=20,
            attribute=DB_STORAGE_QUOTA_SIZE,
        ),
    },
)

service_filemanager_model = models_namespace.model(
    f"Service {services_dict['filemanager'][DICT_SRV_NAME_KEY]}",
    {
        STATUS: fields.String(
            required=False,
            description="Service Status",
            enum=service_status_list,
            example=random.choice(service_status_list),
            attribute=DB_FILEMANAGER_STATUS,
        ),
        MESSAGE: fields.String(
            required=False,
            description="Last action message",
            example="No such file or directory!",
            attribute=DB_FILEMANAGER_MESSAGE,
        ),
        PASSWORD: fields.String(
            required=False,
            description="File-manager login password",
            example="$3kur3",
            attribute=DB_FILEMANAGER_PASSWORD,
        ),
    },
)

service_database_model = models_namespace.model(
    f"Service {services_dict['database'][DICT_SRV_NAME_KEY]}",
    {
        STATUS: fields.String(
            required=False,
            description="Service Status",
            enum=service_status_list,
            example=random.choice(service_status_list),
            attribute=DB_DATABASE_STATUS,
        ),
        MESSAGE: fields.String(
            required=False,
            description="Last action message",
            example="No such file or directory!",
            attribute=DB_DATABASE_MESSAGE,
        ),
        PASSWORD: fields.String(
            required=False,
            description="Project Wordpress DB's password",
            example="$3kur3",
            attribute=DB_DATABASE_PASSWORD,
        ),
        SQL_IMPORT: fields.Boolean(
            required=False,
            description="Determines if user-project sets up with a DB backup import",
            example=True,
            attribute=DB_DATABASE_SQL_IMPORT,
        ),
    },
)

service_wordpress_model = models_namespace.model(
    f"Service {services_dict['wordpress'][DICT_SRV_NAME_KEY]}",
    {
        STATUS: fields.String(
            required=False,
            description="Service Status",
            enum=service_status_list,
            example=random.choice(service_status_list),
            attribute=DB_WORDPRESS_STATUS,
        ),
        MESSAGE: fields.String(
            required=False,
            description="Last action message",
            example="No such file or directory!",
            attribute=DB_WORDPRESS_MESSAGE,
        ),
        PASSWORD: fields.String(
            required=False,
            description="Wordpress dashboard login password",
            example="$3kur3",
            attribute=DB_WORDPRESS_PASSWORD,
        ),
        WP_IMPORT: fields.Boolean(
            required=False,
            description="Determines if user-project sets up with a wordpress file system backup import",
            example=True,
            attribute=DB_WORDPRESS_SQL_IMPORT,
        ),
    },
)

service_nginx_model = models_namespace.model(
    f"Service {services_dict['nginx'][DICT_SRV_NAME_KEY]}",
    {
        STATUS: fields.String(
            required=False,
            description="Service Status",
            enum=service_status_list,
            example=random.choice(service_status_list),
            attribute=DB_NGINX_STATUS,
        ),
        MESSAGE: fields.String(
            required=False,
            description="Last action message",
            example="No such file or directory!",
            attribute=DB_NGINX_MESSAGE,
        ),
        CACHE_KEY: fields.Nested(
            cache_model,
            description="Cache Config",
            allow_null=True,
            skip_none=True,
            attribute=lambda x:x,
        ),
        SSL_CERT_KEY: fields.Nested(
            ssl_model,
            description="SSL Config",
            allow_null=True,
            skip_none=True,
            attribute=lambda x:x,
        ),
    },
)

services_dict["storage"][DICT_SRV_MODEL_KEY] = service_storage_model
services_dict["filemanager"][DICT_SRV_MODEL_KEY] = service_filemanager_model
services_dict["database"][DICT_SRV_MODEL_KEY] = service_database_model
services_dict["wordpress"][DICT_SRV_MODEL_KEY] = service_wordpress_model
services_dict["nginx"][DICT_SRV_MODEL_KEY] = service_nginx_model

services_model = models_namespace.model(
    "Services",
    {
        service_name_list[0]: fields.Nested(
            services_dict[service_name_list[0]][DICT_SRV_MODEL_KEY],
            attribute=lambda x:x,
        ),
        service_name_list[1]: fields.Nested(
            services_dict[service_name_list[1]][DICT_SRV_MODEL_KEY],
            attribute=lambda x:x,
        ),
        service_name_list[2]: fields.Nested(
            services_dict[service_name_list[2]][DICT_SRV_MODEL_KEY],
            attribute=lambda x:x,
        ),
        service_name_list[3]: fields.Nested(
            services_dict[service_name_list[3]][DICT_SRV_MODEL_KEY],
            attribute=lambda x:x,
        ),
        service_name_list[4]: fields.Nested(
            services_dict[service_name_list[4]][DICT_SRV_MODEL_KEY],
            attribute=lambda x:x,
        ),
    },
)

service_name_model = models_namespace.model("Service Name", {
    "service":  fields.String(required=True, description="Service Name", enum=service_name_list, example=random.choice(service_name_list))
})
