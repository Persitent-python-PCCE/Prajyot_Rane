from dao.ticket_dao import TicketDAO

from services.ticket_history_service import TicketHistoryService


class TicketStatusService:

    allowed_transitions = {
        "Open": ["Assigned"],
        "Assigned": ["In Progress"],
        "In Progress": ["Resolved"],
        "Resolved": ["Closed"],
    }

    @staticmethod
    def change_status(ticket_id, new_status, user_id):

        ticket = TicketDAO.find_by_id(ticket_id)

        if not ticket:
            return None, "Ticket not found"

        if not new_status:
            return None, "Status is required"

        old_status = ticket.status

        allowed_statuses = TicketStatusService.allowed_transitions.get(old_status, [])

        if new_status not in allowed_statuses:
            return (
                None,
                f"Invalid status transition: " f"{old_status} -> {new_status}",
            )

        ticket.status = new_status

        TicketDAO.update(ticket)

        TicketHistoryService.add_history(
            ticket_id=ticket_id,
            user_id=user_id,
            action="Status Changed",
            old_value=old_status,
            new_value=new_status,
        )

        return ticket, None
