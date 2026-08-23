from extensions import db
from models.user import User
from services.admin_service import AdminService


def test_deactivate_user(app):

    with app.app_context():

        user = User.query.filter(
            User.is_active.is_(True), User.role.has(name="EMPLOYEE")
        ).first()

        assert user is not None

        original_status = user.is_active

        updated_user, error = AdminService.set_user_status(user.id, False)

        assert error is None
        assert updated_user is not None
        assert updated_user.is_active is False

        updated_user.is_active = original_status
        db.session.commit()
