from models.feedback import Feedback

from dao.feedback_dao import FeedbackDAO
from dao.ticket_dao import TicketDAO

from services.ticket_history_service import TicketHistoryService


class FeedbackService:

    @staticmethod
    def create_feedback(ticket_id, user_id, rating, comment):

        ticket = TicketDAO.find_by_id(ticket_id)

        if not ticket:
            return None, "Ticket not found"

        if ticket.requester_id != user_id:
            return None, "You can only review your own ticket"

        if ticket.status not in ["Resolved", "Closed"]:
            return None, "Feedback can only be submitted after resolution"

        existing = FeedbackDAO.find_by_ticket(ticket_id)

        if existing:
            return None, "Feedback already submitted for this ticket"

        try:
            rating = int(rating)
        except (TypeError, ValueError):
            return None, "Rating must be a number"

        if rating < 1 or rating > 5:
            return None, "Rating must be between 1 and 5"

        feedback = Feedback(
            ticket_id=ticket_id,
            user_id=user_id,
            rating=rating,
            comment=comment.strip() if comment else None,
        )

        FeedbackDAO.save(feedback)

        TicketHistoryService.add_history(
            ticket_id=ticket_id,
            user_id=user_id,
            action="Feedback Submitted",
            old_value=None,
            new_value=f"Rating: {rating}/5",
        )

        return feedback, None
