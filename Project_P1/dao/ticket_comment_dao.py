from extensions import db
from models.ticket_comment import TicketComment


class TicketCommentDAO:

    @staticmethod
    def save(comment):
        db.session.add(comment)
        db.session.commit()
        return comment

    @staticmethod
    def find_by_ticket(ticket_id):
        return (
            TicketComment.query.filter_by(ticket_id=ticket_id)
            .order_by(TicketComment.created_at.asc())
            .all()
        )
