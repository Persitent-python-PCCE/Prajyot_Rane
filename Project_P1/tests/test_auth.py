from extensions import db
from models.user import User
from models.roles import Role


def test_inactive_user_cannot_login(app, client):

    with app.app_context():

        employee_role = Role.query.filter_by(name="EMPLOYEE").first()

        assert employee_role is not None

        user = User.query.filter_by(role_id=employee_role.id).first()

        assert user is not None

        original_status = user.is_active

        user.is_active = False
        db.session.commit()

        response = client.post(
            "/auth/api/login", json={"email": user.email, "password": "123456"}
        )

        assert response.status_code == 401

        data = response.get_json()

        assert data["success"] is False
        assert data["error"] == "Account is inactive"

        user.is_active = original_status
        db.session.commit()
