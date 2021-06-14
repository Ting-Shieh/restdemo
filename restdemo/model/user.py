from werkzeug.security import generate_password_hash, check_password_hash
from restdemo import db
from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
import jwt
from restdemo.model.base import Base
# from flask import current_app
class User(Base):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64))
    tweet = relationship('Tweet')
    def __repr__(self) -> str:
        return "id={}, username={}".format(self.id, self.username)

    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # TODO 抽象化 CRUD db 操作 =>移到base.py
    # def add(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()
    
    # def update(self):
    #     db.session.commit()

    @staticmethod
    def get_by_username(username):
        return db.session.query(User).filter(
            User.username == username
        ).first()

    @staticmethod
    def get_by_id(user_id):
        return db.session.query(User).filter(
            User.id == user_id
        ).first()

    @staticmethod
    def get_user_list():
        return db.session.query(User).all()
    # def generate_token(self):
    #     """生成token 自寫"""

    #     try:
    #         # set up a payload with exciration time
    #         payload ={
    #             'exp': datetime.utcnow() + timedelta(minutes=5),
    #             'iat': datetime.utcnow(),
    #             'sub':self.username,
    #         }
    #         # create the byte string token using the payload and the SECRET key
    #         jwt_token = jwt.encode(
    #             payload,
    #             current_app.config.get('SECRET'),
    #             algorithm='HS256'
    #         )
    #         # return jwt_token.decode()
    #         return jwt_token # 已經是string
            
    #     except Exception as e:
    #         return str(e)
    
    @staticmethod
    def authenticate(username, password):
        user = User.get_by_username(username)

        if user:
            # check password
            if user.check_password(password):
                return user


    @staticmethod
    def identity(payload):
        user_id = payload['identity']
        user = User.get_by_id(user_id)
        return user
