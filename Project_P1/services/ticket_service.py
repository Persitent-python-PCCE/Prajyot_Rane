from models.ticket import Ticket
from dao.ticket_dao import TicketDAO
from dao.ticket_category_dao import TicketCategoryDAO


class TicketService:

    @staticmethod
    def create_ticket(
        title, description, priority, severity, category_id, requester_id
    ):

        category = TicketCategoryDAO.find_by_id(category_id)

        if not category:
            return None, "Invalid ticket category"

        ticket = Ticket(
            title=title.strip(),
            description=description.strip(),
            priority=priority or "Medium",
            severity=severity or "Medium",
            status="Open",
            requester_id=requester_id,
            category_id=category_id,
        )

        TicketDAO.save(ticket)

        return ticket, None

    @staticmethod
    def get_user_tickets(user_id):
        return TicketDAO.find_by_requester(user_id)

    @staticmethod
    def get_ticket(ticket_id):
        return TicketDAO.find_by_id(ticket_id)
