"""User Model"""
users = []

class UserModel:
    """Class user model"""
    def __init__(self):
        """Initialize the user model class"""
        self.db = users

    def add_users(self, firstname, lastname, username, email, password, user_role):
        """Adding new users"""
        payload = {
            'user_id' : len(users) + 1,
            'firstname': firstname, 
            'lastname' : lastname,
            'user_role': user_role,
            'username' : username,
            'email' : email,
            'password' : password      
        }
        self.db.append(payload)
        return self.db 

    def get_all_users(self):
        """Returning all users"""
        return self.db

    def get_user(self, email):
        cur = self.db.cursor
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        if user is None:
            return None
        self.db.commit()
        return user
        