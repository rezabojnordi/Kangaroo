from flask_restx import fields
from . import models_namespace


# Model
CACHE_VALID = "validity_time"
CACHE_STATUS = "status"
CACHE_PATHS = "paths"
# Database
DB_CACHE_VALID = "nginx.cache.cache_valid"
DB_CACHE_STATUS = "nginx.enabled"
DB_CACHE_PATHS = "nginx.paths"



cache_model = models_namespace.model('Cache Config', {
    CACHE_VALID:
        fields.Integer(
            required=True,
            description="Maximum time of cached data being valid in hour",
            example=24,
            min=0,
            default=48,
            attribute=DB_CACHE_VALID,
        ),
    CACHE_STATUS:
        fields.Boolean(
            required=False,
            description="The status of caching feature on webserver",
            example=True,
            default=False,
            attribute=DB_CACHE_STATUS,
        ),
    CACHE_PATHS:
        fields.List(
            fields.String(
                required=True,
                description="Paths to get cached",
                example=["/api", "/test/dir"],
                pattern="^(/[^/ ]*)+/?$"
            ),
            attribute=DB_CACHE_PATHS,
        ),
})
