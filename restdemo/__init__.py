from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt import JWT
db = SQLAlchemy()

# 先有 db 再有user
# table
from restdemo.model.user import User as UserModel
from restdemo.model.tweet import Tweet as TweetModel
from restdemo.resource.user import User, UserList
from restdemo.resource.hellow import Helloworld
from restdemo.resource.tweet import Tweet
# from restdemo.resource.auth import Login # 自寫jwt用
from restdemo.config import app_config

jwt = JWT(None, UserModel.authenticate, UserModel.identity)

def create_app(config_name='development'):
    # 操控資源
    app =  Flask(__name__)
    api =Api(app)

    # db 初始化
    # 之後部屬可以改成mysql
    # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:syting29@localhost:3306/demo"
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(app_config[config_name])
    
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt.init_app(app)
    
    # 註冊: 設定路由(對應關係)
    api.add_resource(Helloworld, '/')
    api.add_resource(User, '/user/<string:username>')
    api.add_resource(UserList, '/users')
    api.add_resource(Tweet, '/tweet/<string:username>')
    # api.add_resource(Login, '/auth/login')

    return app