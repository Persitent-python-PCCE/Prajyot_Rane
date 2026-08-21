from models.ticket_comment import TicketComment
from dao.ticket_comment_dao import TicketCommentDAO
from dao.ticket_dao import TicketDAO


class TicketCommentService:

    @staticmethod
    def add_comment(ticket_id, user_id, comment_text):

        ticket = TicketDAO.find_by_id(ticket_id)

        if not ticket:
            return None, "Ticket not found"

        if not comment_text or not comment_text.strip():
            return None, "Comment cannot be empty"

        comment = TicketComment(
            ticket_id=ticket_id, user_id=user_id, comment=comment_text.strip()
        )

        TicketCommentDAO.save(comment)

        return comment, None

    @staticmethod
    def get_comments(ticket_id):
        return TicketCommentDAO.find_by_ticket(ticket_id)
