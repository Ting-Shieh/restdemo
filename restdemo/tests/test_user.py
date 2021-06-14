import unittest
import json
from restdemo import create_app, db
from restdemo.tests.base import TestBase


class TestLogin(TestBase):

    # TODO 測試用戶創建
    def test_user_create(self):
        url = '/user/{}'.format(self.user_data['username'])
        # TODO post
        res = self.client().post(
            url,
            data=self.user_data
        )


        self.assertEqual(res.status_code, 201)
        res_data = json.loads(res.get_data(as_text = True))
        self.assertEqual(
            res_data.get('username'), 
            self.user_data['username']
            )
        self.assertEqual(
            res_data.get('email'),  
            self.user_data['email']
            )

        
        self.assertEqual(res.status_code, 200)
        res_data = json.loads(res.get_data(as_text = True))
        self.assertEqual(
            res_data.get('message'), 
            'user already exist.'
            )


    def test_user_get(self):
        url = '/user/{}'.format(self.user_data['username'])
        res = self.client().post(
            url,
            data=self.user_data,
        )

        # TODO get
        res = self.client().get(url)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(
            res_data.get('username'), 
            self.user_data['username']
            )
        self.assertEqual(
            res_data.get('email'),  
            self.user_data['email']
            )


    def test_user_get_not_exist(self):
        url = '/user/{}'.format(self.user_data['username'])
        res = self.client().get(url)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_data, {'message': 'user not found'})

    def test_user_delete(self):
        url = '/user/{}'.format(self.user_data['username'])
        # user login
        url = '/auth/login'
        res = self.client().post(
            url,
            data=json.dumps({'username': 'test', 'password': 'test123'}),
            headers={'Content-Type': 'application/json'}
        )
        res_data = json.loads(res.get_data(as_text=True))
        access_token = 'JWT {}'.format(
            # self.app.config['JWT_AUTH_HEADER_PREFIX'],
            res_data['access_token']
        )

        self.client().post(
            url,
            data=self.user_data,
            headers={'Authorization': access_token}
        )
        
        res = self.client().delete(url)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data, {'message': 'user deleted'})

    def test_user_delete_not_exist(self):
        url = '/user/{}'.format(self.user_data['username'])
        res = self.client().delete(url)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_data, {'message': 'user not found'})  

    def test_user_update(self):
        url = '/user/{}'.format(self.user_data['username'])
        self.client().post(
            url,
            data=self.user_data
        )
        res = self.client().put(
            url,
            data={
                'password': 'newpassword',
                'email': 'newemail@new.com'
                }
            )
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data['email'], 'newemail@new.com')
    
    def test_user_update_not_exist(self):
        url = '/user/{}'.format(self.user_data['username'])
        res = self.client().put(
            url,
            data={
                'password': 'newpassword',
                'email': 'newemail@new.com'
                }
            )
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_data, {'message': 'user not found'})  