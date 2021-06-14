  
from datetime import timedelta
import os

class Config:
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:syting29@localhost:3306/demo"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET="flask123" # 自寫
    SECRET_KEY=os.environ.get('SECRET_KEY', 'flask123')
    JWT_EXPIRATION_DELTA = timedelta(seconds=300)
    JWT_AUTH_URL_RULE = "/auth/login"
    JWT_AUTH_HEADER_PREFIX = os.environ.get('JWT_AUTH_HEADER_PREFIX', 'JWT')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestingCongig(Config):

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'



class DevelopmentCongig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:syting29@localhost:3306/demo"

class ProductionCongig(Config):
    pass


app_config={
    'testing':TestingCongig,
    'development':DevelopmentCongig,
    'production':ProductionCongig,
}