from models.ticket import Ticket
from services.ticket_status_service import TicketStatusService
from extensions import db


def test_invalid_status_transition(app):

    with app.app_context():

        ticket = db.session.get(Ticket, 1)

        assert ticket is not None

        invalid_status = {
            "Open": "Resolved",
            "Assigned": "Closed",
            "In Progress": "Closed",
            "Resolved": "In Progress",
            "Closed": "Open",
        }[ticket.status]

        result, error = TicketStatusService.change_status(
            ticket_id=ticket.id, new_status=invalid_status, user_id=1
        )

        assert result is None
        assert error is not None
        assert "Invalid status transition" in error
