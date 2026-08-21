from services.ticket_comment_service import TicketCommentService


class TicketCommentController:

    @staticmethod
    def add_comment(ticket_id, user_id, comment_text):

        return TicketCommentService.add_comment(ticket_id, user_id, comment_text)

    @staticmethod
    def get_comments(ticket_id):

        return TicketCommentService.get_comments(ticket_id)
