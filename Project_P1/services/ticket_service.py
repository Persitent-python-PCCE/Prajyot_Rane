from models.ticket import Ticket

from dao.ticket_dao import TicketDAO
from dao.ticket_category_dao import TicketCategoryDAO

from services.sla_service import SlaService
from services.ticket_history_service import TicketHistoryService


class TicketService:

    @staticmethod
    def create_ticket(
        title, description, priority, severity, category_id, requester_id
    ):
        category = TicketCategoryDAO.find_by_id(category_id)

        if not category:
            return None, "Invalid ticket category"

        priority = priority or "Medium"
        severity = severity or "Medium"

        sla, error = SlaService.calculate_sla(priority)

        if error:
            return None, error

        ticket = Ticket(
            title=title.strip(),
            description=description.strip(),
            priority=priority,
            severity=severity,
            status="Open",
            requester_id=requester_id,
            category_id=category_id,
            response_due_at=sla["response_due_at"],
            resolution_due_at=sla["resolution_due_at"],
        )

        TicketDAO.save(ticket)

        TicketHistoryService.add_history(
            ticket_id=ticket.id,
            user_id=requester_id,
            action="Ticket Created",
            old_value=None,
            new_value="Open",
        )

        return ticket, None

    @staticmethod
    def get_user_tickets(user_id, page=1, per_page=10):
        return TicketDAO.find_by_requester(user_id, page=page, per_page=per_page)

    @staticmethod
    def get_ticket(ticket_id):
        return TicketDAO.find_by_id(ticket_id)
