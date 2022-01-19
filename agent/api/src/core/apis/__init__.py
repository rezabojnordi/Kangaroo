from flask_restx import Api


api = Api(
    version="1.0.1",
    title="Kangero API",
    description="The infrastructure's middleware API list which WUI backend can interact with",
    validate=True,
)

# Import all namespaces consisting resources and models.
# When they're imported, they're already added to `api` object.
import apis.resources
import apis.models
