"""User Model"""
from app.db_config import init_db

class UserModel:
    """Class user model"""
    def __init__(self):
        """Initialize the user model class"""
        self.db = init_db()

    def add_users(self, firstname, lastname, user_role, username, email, password):
        """Adding new users"""
        query = "INSERT INTO users (firstname, lastname, user_role, username, \
         email, password) VALUES (%s,%s,%s,%s,%s,%s)"
        cur = self.db.cursor()
        cur.execute(query, (firstname, lastname, user_role, username, email, \
         password))
        self.db.commit() 

    def get_one_user(self, username):
        pass
        