from models.ticket_history import TicketHistory
from dao.ticket_history_dao import TicketHistoryDAO


class TicketHistoryService:

    @staticmethod
    def add_history(ticket_id, user_id, action, old_value=None, new_value=None):

        history = TicketHistory(
            ticket_id=ticket_id,
            user_id=user_id,
            action=action,
            old_value=old_value,
            new_value=new_value,
        )

        TicketHistoryDAO.save(history)

        return history

    @staticmethod
    def get_history(ticket_id):
        return TicketHistoryDAO.find_by_ticket(ticket_id)
