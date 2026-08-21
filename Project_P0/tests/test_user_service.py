import bcrypt
from services.user_service import UserService
from models.user import Admin, Customer


def test_login_success_customer():
    service = UserService()
    password_hash = bcrypt.hashpw(b"123", bcrypt.gensalt()).decode("utf-8")
    # Mock DAO response
    service.user_dao.get_login_details = lambda email: (
        1,
        "Leo",
        password_hash,
        "user",
        "leomessi@goat.com",
    )
    user = service.login_user("leomessi@goat.com", "123")
    assert user is not None
    assert isinstance(user, Customer)
    assert user.u_id == 1
    assert user.username == "Leo"
    assert user.role == "user"


def test_login_success_admin():

    service = UserService()

    password_hash = bcrypt.hashpw(b"admin123", bcrypt.gensalt()).decode("utf-8")

    service.user_dao.get_login_details = lambda email: (
        2,
        "Admin",
        password_hash,
        "admin",
        "admin@email.com",
    )

    user = service.login_user("admin@email.com", "admin123")

    assert user is not None
    assert isinstance(user, Admin)
    assert user.u_id == 2
    assert user.username == "Admin"
    assert user.role == "admin"


def test_login_invalid_email():

    service = UserService()

    service.user_dao.get_login_details = lambda email: None

    user = service.login_user("wrong@email.com", "123")

    assert user is None


def test_login_incorrect_password():

    service = UserService()

    password_hash = bcrypt.hashpw(b"123", bcrypt.gensalt()).decode("utf-8")

    service.user_dao.get_login_details = lambda email: (1, "Leo", password_hash, "user")

    user = service.login_user("leomessi@goat.com", "wrongpassword")

    assert user is None
