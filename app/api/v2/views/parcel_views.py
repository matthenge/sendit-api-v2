"""Parcel views"""
from flask_restful import Resource, reqparse
from app.db_config import init_db
from app.api.v2.models.parcel_models import ParcelModel

orders = ParcelModel()

class OrderCreation(Resource):
    """Class for parcel creation"""

    def __init__(self):
        self.order_parser = reqparse.RequestParser()
        self.order_parser.add_argument("pickup_location", type=str, required=True)
        self.order_parser.add_argument("current_location", type=str, required=True)
        self.order_parser.add_argument("destination", type=str, required=True)
        self.order_parser.add_argument("price", type=str, required=True)
        self.order_parser.add_argument("status", type=str, required=True)
        self.order_parser.add_argument("user_id", type=str, required=True)

    def post(self):
        """Order creation"""
        data = self.order_parser.parse_args()
        pickup_location = data["pickup_location"]
        current_location = data["current_location"]
        destination = data["destination"]
        price = data["price"]
        status = data["status"]
        user_id = data["user_id"]
        
        orders.create_parcels(pickup_location, current_location, destination, price, status, user_id)
        return {
            "message": "Order placed successful"
        }, 201
