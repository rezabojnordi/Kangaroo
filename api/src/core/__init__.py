from flask import Flask
from apis import api


# Here's the Flask app factory!
def create_app():
    app = Flask(__name__)
    # TODO: Read from a config.py file or something
    app.config['RESTX_MASK_SWAGGER'] = False
    api.init_app(app)

    return app
