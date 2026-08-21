from services.auth_service import AuthService


class AuthController:

    @staticmethod
    def register(name, email, password):

        if not name or not email or not password:
            return None, "All fields are required"

        if len(name.strip()) < 2:
            return None, "Name must contain at least 2 characters"

        if len(password) < 6:
            return None, "Password must contain at least 6 characters"

        user, error = AuthService.register_user(name, email, password)

        if error:
            return None, error

        return user, None

    @staticmethod
    def login(email, password):

        if not email or not password:
            return None, "Email and password are required"

        user = AuthService.login_user(email, password)

        if not user:
            return None, "Invalid email or password"

        return user, None

    @staticmethod
    def has_role(required_roles, current_role):

        if current_role not in required_roles:
            return False

        return True
