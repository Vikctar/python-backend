import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    APP_NAME = os.getenv('APP_NAME')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APIFAIRY_TITLE = os.getenv('APIFAIRY_TITLE')
    APIFAIRY_VERSION = os.getenv('APIFAIRY_VERSION')
    APIFAIRY_UI = os.getenv('APIFAIRY_UI')


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL')


class TestingConfig(Config):
    SECRET_KEY = '8dad8aeaffc12e82'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL') or 'sqlite://'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
