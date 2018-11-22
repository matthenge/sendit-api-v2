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

    def get_all_users(self):
        """Returning all users"""
        return self.db

class FetchUser:
    def __init__(self):
        """Initialize the user model class"""
        self.db = init_db()

    def get_user(self, email):
        cur = self.db.cursor
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        if user is None:
            return None
        self.db.commit()
        return user
