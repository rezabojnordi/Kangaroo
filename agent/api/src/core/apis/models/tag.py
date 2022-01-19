from flask_restx import fields
from . import models_namespace


# Model
TAG = "tag"
# Database
DB_TAG = TAG


# Note: WUI Backend will control the tag values and we don't
tag_model = models_namespace.model(
    "Tag",
    {
        TAG: fields.String(
            required=True,
            description="User-project's tag content",
            example="verified",
            attribute=DB_TAG,
        ),
    },
)
