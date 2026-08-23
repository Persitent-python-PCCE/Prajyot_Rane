from services.ticket_service import TicketService


class TicketController:

    @staticmethod
    def create_ticket(
        title, description, priority, severity, category_id, requester_id
    ):

        if not title or not description:
            return None, "Title and description are required"

        if not category_id:
            return None, "Category is required"

        if not priority:
            priority = "Medium"

        if not severity:
            severity = "Medium"

        ticket, error = TicketService.create_ticket(
            title, description, priority, severity, category_id, requester_id
        )

        if error:
            return None, error

        return ticket, None

    @staticmethod
    def get_user_tickets(user_id, page=1, per_page=10):
        return TicketService.get_user_tickets(user_id, page=page, per_page=per_page)

    @staticmethod
    def get_ticket(ticket_id):

        return TicketService.get_ticket(ticket_id)
