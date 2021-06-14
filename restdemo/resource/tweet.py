from flask_restful import Resource, reqparse
from restdemo.model.user import User as UserModel
from restdemo.model.tweet import Tweet as TweetModel

from flask_jwt import jwt_required, current_identity

class Tweet(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'body',
        type=str,
        required=True,
        help="body is required"
    )

    #　token 鎖定  user
    @jwt_required()
    def post(self, username):

        # 驗證用戶 是否和 token用戶 相同
        if current_identity.username != username:
            return {"message": "please use the right token."}, 404
        user = UserModel.get_by_username(username)
        if not user:
            return {"message": "user not found"}, 404
        # 這個要用自己 class 自帶ㄉ
        data = Tweet.parser.parse_args()
        tweet = TweetModel(body=data['body'], user_id=user.id)
        tweet.add()
        return  {"message": "tweet add  successfully"}, 201

    # user 是誰 token 無所謂
    @jwt_required()
    def get(self, username):
        user = UserModel.get_by_username(username)
        if not user:
            return {"message": "user not found"}, 404
        return [t.as_dict() for t in user.tweet]