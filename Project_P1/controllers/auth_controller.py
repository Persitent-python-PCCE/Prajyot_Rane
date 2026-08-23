from flask import session

from services.auth_service import AuthService


class AuthController:

    @staticmethod
    def register_user(name, email, password):

        if not name or not email or not password:
            return None, "All fields are required"

        if len(name.strip()) < 2:
            return None, "Name must contain at least 2 characters"

        if len(password) < 6:
            return None, "Password must contain at least 6 characters"

        return AuthService.register_user(name, email, password)

    @staticmethod
    def login_user(email, password):

        if not email or not password:
            return None, "Email and password are required"

        user, error = AuthService.login_user(email, password)

        if error:
            return None, error

        session["user_id"] = user.id
        session["user_name"] = user.name
        session["role"] = user.role.name

        return user, None

    @staticmethod
    def logout_user():

        session.clear()

    @staticmethod
    def has_role(roles, current_role):

        return current_role in roles
