from flask_restful import Resource, reqparse
from restdemo import db
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

class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'password',
        type=min_length_str(5),
        required=True,
        help='{error_msg}'
        )
    parser.add_argument(
        'username', 
        type=str, 
        required=True, 
        help='required username'
    )
    def post(self):
        data = Login.parser.parse_args()
        user = db.session.query(UserModel).filter(
            UserModel.username == data['username']
        ).first()
        if user:
            if not user.check_password(data['password']):
                return {'message': '登入失敗，請輸入正確帳號或密碼.'}
            # 生成token
            return {
                "message":"login success",
                "token": user.generate_token()
            }
        else:
            return {
                "message":"login failed",
            }
       
