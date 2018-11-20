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

    def get_one_user(self, username):
        """Return a specific user"""
        for user in self.db:
            if user['username'] == str(username):
                return {
                    "message": "User found", "User Details": user
                }, 200
        return {
            "Error": "User not found!"
        }, 200



 
