"""User views"""
from flask_restful import Resource, reqparse
from app.db_config import init_db
from app.api.v2.models.user_models import UserModel

users = UserModel()

class UserRegistration(Resource):
    """Class for user registration"""

    def __init__(self):
        self.user_parser = reqparse.RequestParser()
        self.user_parser.add_argument("firstname", type=str, required=True)
        self.user_parser.add_argument("lastname", type=str, required=True)
        self.user_parser.add_argument("user_role", type=str, required=True)
        self.user_parser.add_argument("username", type=str, required=True)
        self.user_parser.add_argument("email", type=str, required=True)
        self.user_parser.add_argument("password", type=str, required=True)

    def post(self):
        """User signup"""
        data = self.user_parser.parse_args()
        firstname = data["firstname"]
        lastname = data["lastname"]
        user_role = data["user_role"]
        username = data["username"]
        email = data["email"]
        password = data["password"]
        
        users.add_users(firstname, lastname, user_role, username,email, password)
        return {
            "message": "Sign up successful"
        }, 201
