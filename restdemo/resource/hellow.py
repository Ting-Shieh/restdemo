
from flask_restful import Resource

# 利用 class 操作
class Helloworld(Resource):   
    def get(self):
        return 'hellow'