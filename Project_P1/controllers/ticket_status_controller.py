from services.ticket_status_service import TicketStatusService


class TicketStatusController:

    @staticmethod
    def change_status(ticket_id, new_status, user_id):

        return TicketStatusService.change_status(ticket_id, new_status, user_id)
