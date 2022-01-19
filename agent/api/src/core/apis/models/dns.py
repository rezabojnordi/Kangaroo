from flask_restx import fields
from . import models_namespace


dns_model = models_namespace.model(
    "DNS Config",
    {
        "value": fields.String(
            required=True,
            description="?????",
            pattern=".?",
            example="?????"
        ),
    },
)
