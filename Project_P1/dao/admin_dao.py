from models.user import User
from models.ticket import Ticket
from models.roles import Role
from extensions import db


class AdminDAO:

    @staticmethod
    def get_support_agents():
        return (
            User.query.join(User.role)
            .filter_by(name="SUPPORT_AGENT")
            .order_by(User.name)
            .all()
        )

    @staticmethod
    def get_all_tickets():
        return Ticket.query.order_by(Ticket.created_at.desc()).all()

    @staticmethod
    def save_user(user):
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def find_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_role_by_name(name):
        return Role.query.filter_by(name=name).first()
