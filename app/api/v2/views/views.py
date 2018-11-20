"""Version 2 views"""
from flask import jsonify, make_response, request
from flask_restful import Resource
from app.api.v2.models.parcels_model import Parcels
from app.api.v2.models.user_models import UserModel
from flask_restful.reqparse import RequestParser

parcel = Parcels()
users = UserModel()

class CreateOrder(Resource):
    """Class for creating order"""
    def __init__(self):
        self.order_parser = RequestParser()
        self.order_parser.add_argument("pickup_location", type=str, required=True, help="Please enter a pickup location")
        self.order_parser.add_argument("destination", type=str, required=True, help="Please enter a destination")
        self.order_parser.add_argument("price", type=str, required=True, help="Invalid price")
        self.order_parser.add_argument("user_id", type=str, required=True, help="invalid user_id")

    def post(self):
        """Create order endpoint"""
        data = self.order_parser.parse_args()
        data = request.get_json()
        pickup_location = data['pickup_location']
        destination = data['destination']
        price = data['price']
        user_id = data['user_id']

        parcel.create_orders(pickup_location, destination, price, user_id)
        return {
            "message": "Order placed Successfully"
        }, 201

class ReturnOneOrder(Resource):
    """Specific order endpoints"""
    def get(self, order_id):
        """GET specific order"""
        try:
            int(order_id)
        except ValueError:
            return {
                "Error": "Please enter a valid order number"
            }, 400
        one_order = parcel.get_specific_order(order_id)
        return one_order
            
class CancelOrder(Resource):
    """Order cancellation"""
    def put(self, order_id):
        """Cancel order"""
        try:
            int(order_id)
        except ValueError:
            return {
                "Error": "Please enter a valid order number"
            }, 400
        cancel = parcel.cancel_order(order_id)
        return cancel

class AllOrders(Resource):
    """Class for all order views"""
    def get(self):
        """Return all orders"""
        all_orders = parcel.get_all_orders()
        return {
            "message": "Success", "Orders": all_orders
        }, 200

class UserParcels(Resource):
    """Class for single user operations"""
    def get(self, user_id):
        """Get all orders by a specific user"""
        try:
            int(user_id)
        except ValueError:
            return {
                "Error": "Please enter a valid user ID"
            }, 400
        all_user_orders = parcel.get_orders_by_specific_user(user_id)
        return all_user_orders
        
class CreateUser(Resource):
    """Class for single user operations"""
    def __init__(self):
        self.user_parser = RequestParser()
        self.user_parser.add_argument("firstname", type=str, required=True, help="Please enter a firstname")
        self.user_parser.add_argument("lastname", type=str, required=True, help="Please enter a lastname")
        self.user_parser.add_argument("user_role", type=str, required=True, help="invalid user role")
        self.user_parser.add_argument("username", type=str, required=True, help="Please enter a username")
        self.user_parser.add_argument("email", type=str, required=True, help="Please enter a valid email")
        self.user_parser.add_argument("password", type=str, required=True, help="Please enter a password")

    def post(self):
        """Create user"""
        data = request.get_json()
        firstname = data['firstname']
        lastname = data['lastname']
        user_role = data['user_role']
        username = data['username']
        email = data['email']
        password = data['password']

        users.add_users(firstname, lastname, user_role, username, email, password)
        return{
            "message": "successful registration"
        }, 201

class ReturnUser(Resource):
    """Retrieve user"""
    def get(self, username):
        """Get a user using the username"""
        user = users.get_one_user(username)
        return user

class ReturnAllUsers(Resource):
    """Return all users"""
    def get(self):
        """Get all users"""
        all_users = users.get_all_users()
        return {
            "message": "success", "users": all_users 
        }
