import json

from apifairy import APIFairy
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from config import config

apifairy = APIFairy()
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
limiter = Limiter(key_func=get_remote_address)


def create_app(config_class='default'):
    """"
    Allows creation of application using different configurations
    :param config_class:
    :return: app
    """
    app = Flask(__name__)
    app.config.from_object(config[config_class])

    initialize_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)

    return app


def initialize_extensions(app):
    apifairy.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    limiter.init_app(app)


def register_blueprints(app):
    from app.api import api

    app.register_blueprint(api)


def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        """Return JSON instead of HTML for HTTP errors"""
        # Start with the correct headers and status code from the error
        response = e.get_response()
        # Replaces the body with JSON
        response.data = json.dumps({
            'code': e.code,
            'name': e.name,
            'description': e.description
        })
        response.content_type = 'application/json'
        return response

from app import models, schemas
