from datetime import datetime

from extensions import db
from models.ticket import Ticket


class TicketDAO:

    @staticmethod
    def save(ticket):
        db.session.add(ticket)
        db.session.commit()
        return ticket

    @staticmethod
    def find_by_id(ticket_id):
        return db.session.get(Ticket, ticket_id)

    @staticmethod
    def find_by_requester(requester_id, page=1, per_page=10):
        return (
            Ticket.query.filter_by(requester_id=requester_id)
            .order_by(Ticket.created_at.desc())
            .paginate(page=page, per_page=per_page, error_out=False)
        )

    @staticmethod
    def update(ticket):
        db.session.commit()
        return ticket

    @staticmethod
    def find_sla_breaches():
        now = datetime.now()

        return (
            Ticket.query.filter(
                ((Ticket.response_due_at < now) | (Ticket.resolution_due_at < now)),
                Ticket.status != "Closed",
            )
            .order_by(Ticket.created_at.asc())
            .all()
        )
