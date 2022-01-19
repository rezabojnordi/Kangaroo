from flask_restx import Namespace
from apis import api

models_namespace = Namespace("models", description="List of API models")
# Import all models defined in sub-modules
from . import *

# Add them to the only model namespace
api.add_namespace(models_namespace)
