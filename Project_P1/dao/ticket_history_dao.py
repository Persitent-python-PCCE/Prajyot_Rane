from extensions import db
from models.ticket_history import TicketHistory


class TicketHistoryDAO:

    @staticmethod
    def save(history):
        db.session.add(history)
        db.session.commit()
        return history

    @staticmethod
    def find_by_ticket(ticket_id):
        return (
            TicketHistory.query.filter_by(ticket_id=ticket_id)
            .order_by(TicketHistory.created_at.asc())
            .all()
        )

    @staticmethod
    def exists_for_action(ticket_id, action):
        return (
            TicketHistory.query.filter_by(ticket_id=ticket_id, action=action).first()
            is not None
        )
