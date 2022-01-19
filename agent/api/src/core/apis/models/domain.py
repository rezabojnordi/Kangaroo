from flask_restx import fields
from . import models_namespace


# Model
DOMAIN = "domain"
# Database
DB_DOMAIN = "domain_name"


domain_model = models_namespace.model(
    "Domain",
    {
        DOMAIN: fields.String(
            required=True,
            description="Project domain address",
            example="example.com",
            pattern="^(((?!-))(xn--|_{1,1})?[a-z0-9-]{0,61}[a-z0-9]{1,1}\.)*(xn--)?([a-z0-9][a-z0-9\-]{0,60}|[a-z0-9-]{1,30}\.[a-z]{2,})$",
            attribute=DB_DOMAIN,
        ),
    },
)
