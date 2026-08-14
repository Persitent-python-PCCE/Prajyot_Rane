from services.user_service import UserService, Admin, Customer


def test_login_success_customer():

    service = UserService()

    # Mock DAO response
    service.user_dao.get_login_details = lambda email: (1, "Leo", "123", "user")

    user = service.login_user("leomessi@goat.com", "123")

    assert user is not None
    assert isinstance(user, Customer)
    assert user.u_id == 1
    assert user.username == "Leo"
    assert user.role == "user"


def test_login_success_admin():

    service = UserService()

    service.user_dao.get_login_details = lambda email: (2, "Admin", "admin123", "admin")

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

    service.user_dao.get_login_details = lambda email: (1, "Leo", "123", "user")

    user = service.login_user("leomessi@goat.com", "wrongpassword")

    assert user is None
