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
        return Ticket.query.get(ticket_id)

    @staticmethod
    def find_by_requester(requester_id):
        return (
            Ticket.query.filter_by(requester_id=requester_id)
            .order_by(Ticket.created_at.desc())
            .all()
        )

    @staticmethod
    def update(ticket):
        db.session.commit()
        return ticket
