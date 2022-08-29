from apifairy import APIFairy
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import config

apifairy = APIFairy()
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


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

    return app


def initialize_extensions(app):
    apifairy.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)


def register_blueprints(app):
    from app.api import api

    app.register_blueprint(api)
