import bcrypt
from dao.user_dao import UserDao
from models.user import User, Admin, Customer


class UserService:
    def __init__(self):
        self.user_dao = UserDao()

    def register_user(self, username, password, email):
        if not username:
            print("Username cannot be empty")
            return
        if not password:
            print("Password cannot be empty")
            return
        if not email:
            print("Email cannot be Empty")
            return

        hash_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        self.user_dao.get_user(username, hash_password.decode("utf-8"), email)
        print("Registration Successfull")

    def login_user(self, email, password):
        user = self.user_dao.get_login_details(email)
        if user is None:
            print("email does not exist!")
            return
        if not bcrypt.checkpw(password.encode("utf-8"), user[2].encode("utf-8")):
            print("Incorrect Password!")
            return None
        print("\nLogin Successful!")
        if user[3] == "admin":
            return Admin(user[0], user[1], user[4])
        else:
            return Customer(user[0], user[1], user[4])
