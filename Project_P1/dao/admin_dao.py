from sqlalchemy import func

from extensions import db

from models.user import User
from models.ticket import Ticket
from models.roles import Role
from models.ticket_assignment import TicketAssignment


class AdminDAO:

    @staticmethod
    def get_support_agents():
        return (
            User.query.join(User.role)
            .filter(Role.name == "SUPPORT_AGENT")
            .order_by(User.name)
            .all()
        )

    @staticmethod
    def get_all_tickets():
        return Ticket.query.order_by(Ticket.created_at.desc()).all()

    @staticmethod
    def find_tickets(
        status=None,
        priority=None,
        severity=None,
        category_id=None,
        requester_id=None,
        agent_id=None,
        page=1,
        per_page=10,
    ):
        query = Ticket.query

        if status:
            query = query.filter(Ticket.status == status)

        if priority:
            query = query.filter(Ticket.priority == priority)

        if severity:
            query = query.filter(Ticket.severity == severity)

        if category_id:
            query = query.filter(Ticket.category_id == category_id)

        if requester_id:
            query = query.filter(Ticket.requester_id == requester_id)

        if agent_id:
            query = query.join(
                TicketAssignment, TicketAssignment.ticket_id == Ticket.id
            ).filter(TicketAssignment.agent_id == agent_id)

        return query.order_by(Ticket.created_at.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )

    @staticmethod
    def get_ticket_status_counts():
        return (
            Ticket.query.with_entities(Ticket.status, func.count(Ticket.id))
            .group_by(Ticket.status)
            .all()
        )

    @staticmethod
    def get_ticket_priority_counts():
        return (
            Ticket.query.with_entities(Ticket.priority, func.count(Ticket.id))
            .group_by(Ticket.priority)
            .all()
        )

    @staticmethod
    def get_ticket_category_counts():
        return (
            Ticket.query.with_entities(Ticket.category_id, func.count(Ticket.id))
            .group_by(Ticket.category_id)
            .all()
        )

    @staticmethod
    def get_all_users():
        return User.query.join(User.role).order_by(User.id.asc()).all()

    @staticmethod
    def search_users(search=None, page=1, per_page=10):
        query = User.query

        if search:
            search = f"%{search.strip()}%"

            query = query.filter(
                db.or_(User.name.ilike(search), User.email.ilike(search))
            )

        return query.order_by(User.id.asc()).paginate(
            page=page, per_page=per_page, error_out=False
        )

    @staticmethod
    def find_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_role_by_name(name):
        return Role.query.filter_by(name=name).first()

    @staticmethod
    def save_user(user):
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def find_user_by_id(user_id):
        return db.session.get(User, user_id)

    @staticmethod
    def update_user(user):
        db.session.commit()
        return user
