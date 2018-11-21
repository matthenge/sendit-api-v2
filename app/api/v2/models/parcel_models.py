"""Parcels model"""
from app.db_config import init_db

class ParcelModel:
    """Class parcel model"""
    def __init__(self):
        """Initialize the user model class"""
        self.db = init_db()

    def create_parcels(self, pickup_location, current_location, destination, price, status, user_id):
        """Adding new users"""
        query = "INSERT INTO orders (pickup_location, current_location, destination, price, \
         status, user_id) VALUES (%s,%s,%s,%s,%s,%s)"
        cur = self.db.cursor()
        cur.execute(query, (pickup_location, current_location, destination, price, status, user_id))
        self.db.commit()
        