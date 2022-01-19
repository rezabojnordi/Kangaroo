from flask_restx import fields
from . import models_namespace


# Model
SSL_CONTENT_PUB = "ssl_base64_pub_content"
SSL_CONTENT_PRIV = "ssl_base64_priv_content"
# Database
DB_SSL_PUB = "nginx.certificate.pub"
DB_SSL_PRIV = "nginx.certificate.priv"


ssl_model = models_namespace.model('SSL Config', {
    SSL_CONTENT_PUB:
        fields.String(
            required=True,
            description="SSL full chain file content in base64 form",
            example="LS0tLS1CRUdJTiBDRVJUSUZJQ0FU...",
            attribute=DB_SSL_PUB,
        ),
    SSL_CONTENT_PRIV:
        fields.String(
            required=True,
            description="SSL private chain file content in base64 form",
            example="Rm9sbG93aW5nIGFyZSB0aGU...",
            attribute=DB_SSL_PRIV,
        ),
})
