from extensions import db
from models.ticket_assignment import TicketAssignment


class TicketAssignmentDAO:

    @staticmethod
    def save(assignment):
        db.session.add(assignment)
        db.session.commit()
        return assignment

    @staticmethod
    def find_by_ticket(ticket_id):
        return (
            TicketAssignment.query.filter_by(ticket_id=ticket_id)
            .order_by(TicketAssignment.assigned_at.desc())
            .all()
        )

    @staticmethod
    def find_current_assignment(ticket_id):
        return (
            TicketAssignment.query.filter_by(ticket_id=ticket_id)
            .order_by(TicketAssignment.assigned_at.desc())
            .first()
        )
