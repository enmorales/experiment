import os
from dotenv import load_dotenv
load_dotenv()

class ConfigClass(object):
    SECRET_KEY = os.getenv('SECRET_KEY', '')
    CONTAINER = os.getenv('CONTAINER', '')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', '')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', '')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', '')
    JWT_ACCESS_TOKEN_EXPIRES = os.getenv('JWT_ACCESS_TOKEN_EXPIRES', '')
    POSTGRES_URL = os.getenv('POSTGRES_URL', '')
    PERFILES_MS = os.getenv('PERFILES_MS', '')
    AMBIENTE = os.getenv('AMBIENTE', '')