# restful api 已經把 return 數據做一次 jsonify 處理
# reqparse => 做 參數檢查
from flask_jwt import jwt_required,current_identity
from flask_migrate import current
from flask_restful import Resource, reqparse
# 自己寫 jwt
# import jwt 
# from flask import current_app, request
# from restdemo import db
from restdemo.model.user import User as UserModel


def min_length_str(min_length):
    def validate(s):
        if s is None:
            raise Exception('password required')
        if not isinstance(s, (int, str)):
            raise Exception('password format error')
        if len(s) >= min_length:
            return str(s)
        raise Exception("String must be at least %i characters long"% min_length)
    return validate

class User(Resource):
    # 過濾參數
    parser = reqparse.RequestParser()
    parser.add_argument(
        'password',
        type=min_length_str(5),
        required=True,
        help='{error_msg}'
        )
    parser.add_argument(
        'email', type=str, required=True, help='required email'
    )
    def get(self, username):
        """get user detail"""
        user = UserModel.get_by_username(username)
        
        if user:
            return user.as_dict()
          
        return {'message': 'user not found'}, 404 

    def post(self, username):
        
        data = User.parser.parse_args()
        user = UserModel.get_by_username(username)
        if user:
            return {'message': 'user already exist.'}
        newuser = UserModel(
            username=username,
            email=data['email']
        )
        newuser.set_password(data['password'])
        newuser.add()
        return newuser.as_dict(), 201
    @jwt_required()
    def put(self, username):
        # 驗證用戶 是否和 token用戶 相同
        if current_identity.username != username:
            return {"message": "please use the right token."}, 404
        user = UserModel.get_by_username(username)
        
        if user:
            data = User.parser.parse_args()
            user.email = data['email']
            user.set_password(data['password'])
            user.update()
            return user.as_dict()

        else:
            return {'message': 'user not found'}, 404
    @jwt_required()
    def delete(self, username):
        # 驗證用戶 是否和 token用戶 相同
        if current_identity.username != username:
            return {"message": "please use the right token."}, 404
        
        user = UserModel.get_by_username(username)
        # 找到        
        if user:
            user.delete()
            return {'message': 'user deleted'}

        else:
            return {'message': 'user not found'}, 404

class UserList(Resource):
    # def get(self):
    #     # TODO 自寫版
    #     # 驗證 token
    #     token  = request.headers.get('Authorization')

    #     try:
    #         jwt.decode(
    #             token,
    #             current_app.config.get("SECRET"),
    #             algorithms="HS236"
    #         )
    #     except jwt.ExpiredSignatureError:
    #         return {'message': 'Expired Token.請重新登入或註冊!!'}
    #     except jwt.InvalidTokenError:
    #         return {'message': 'Invalid Token.請重新登入或註冊!!'}
        
    #     users = db.session.query(UserModel).all()
    #     return [u.as_dict() for u in users]

    @jwt_required()
    def get(self):  
        users = UserModel.get_user_list()
        return [u.as_dict() for u in users]