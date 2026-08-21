import bcrypt

from models.user import User
from dao.user_dao import UserDAO
from dao.role_dao import RoleDAO


class AuthService:

    @staticmethod
    def register_user(name, email, password):

        email = email.strip().lower()

        existing_user = UserDAO.find_by_email(email)

        if existing_user:
            return None, "Email already registered"

        employee_role = RoleDAO.find_by_name("EMPLOYEE")

        if not employee_role:
            return None, "Employee role not found"

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")

        user = User(
            name=name.strip(),
            email=email,
            password=hashed_password,
            role_id=employee_role.id,
        )

        UserDAO.save(user)

        return user, None

    @staticmethod
    def login_user(email, password):

        email = email.strip().lower()

        user = UserDAO.find_by_email(email)

        if not user:
            return None

        if bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
            return user

        return None
