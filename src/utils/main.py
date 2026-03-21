import os
import logging
from flask import Flask
from flask_cors import CORS
from api_service.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app)

    from api_service.api import api
    app.register_blueprint(api, url_prefix='/api')

    if not os.path.exists('logs'):
        os.makedirs('logs')

    logging.basicConfig(filename='logs/app.log', level=logging.INFO)

    return app

app = create_app()