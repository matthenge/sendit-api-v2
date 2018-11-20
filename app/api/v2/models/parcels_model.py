"""Parcels model"""
from app.api.v2.models.user_models import UserModel
orders = []

class Parcels:
    """The Parcels class"""

    def __init__(self):
        self.db = orders
        self.order_status = 'pending'

    def create_orders(self, pickup_location, destination, price, user_id):
        """Create orders"""
        payload = {
            'order_id' : len(orders) + 1,
            'pickup_location': pickup_location, 
            'destination' : destination,
            'status': self.order_status,
            'price' : price, 
            'user_id' : user_id   
        }
        self.db.append(payload)
        return self.db

    def get_all_orders(self):
        """Return all orders"""
        return self.db

    def get_specific_order(self, order_id):
        """Return a specific order"""
        for order in self.db:
            if order['order_id'] == int(order_id):
                return {
                     "message": "Order retrieved", "Order" : order
                    }, 200 
        return {
                "Error": "Order not found!"
                    }, 200
                          

    def get_orders_by_specific_user(self, user_id):
        """Return all orders by a specific user"""
        user_orders = []
        for order in self.db:
            if order['user_id'] == user_id:
                user_orders.append(order)
        if not user_orders:
            return{
                "message": "User does not have orders"
            }, 200
        return {
             "message": "user orders", "User Orders": user_orders
            }, 200

    def cancel_order(self, order_id):
        """Cancel an order"""
        for order in self.db:
            if order['order_id'] == int(order_id):
                if order['status'] == 'pending':
                    order.update({'status': 'cancelled'})
                    return {
                        "message" : "Order cancelled"
                    }, 200
                elif order['status'] == 'cancelled':
                    return{
                        "Error":"Order has already been cancelled"
                    }, 200
                elif order['status'] == 'delivered':
                    return{
                        "Error": "Order already delivered"
                    }, 200
