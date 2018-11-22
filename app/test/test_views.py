"""Tests"""
import unittest
import json
from app import create_app
     
class TestViews(unittest.TestCase):
    """Tests class"""
    def setUp(self):
        """set up method for tests"""
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app

        self.order = {
            "order_id":"100",
            "pickup_location":"nakuru",
            "destination":"nairobi",
            "price":"1400",
            "user_id":"5"

        }
        self.user = {
            "firstname":"James",
            "lastname":"Martin",
            "user_role":"Admin",
            "username":"arc",
            "email":"arc@yahoo.com",
            "password":"andela"
        }
    def test_post(self):
        """test register user"""
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.user), content_type='application/json')
        self.assertIn("Sign up successful", str(response.data))
        self.assertEqual(response.status_code, 201)
