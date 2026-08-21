class User:
    def __init__(self, username, email, u_id, role):
        self.u_id = u_id
        self.username = username
        self.email = email
        self.role = role

    def display_users(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Role: {self.role}")


class Admin(User):
    def __init__(self, u_id, username, email):
        super().__init__(username, email, u_id, "admin")


class Customer(User):
    def __init__(self, u_id, username, email):
        super().__init__(username, email, u_id, "user")
