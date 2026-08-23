from services.feedback_service import FeedbackService


class FeedbackController:

    @staticmethod
    def create_feedback(ticket_id, user_id, rating, comment):

        return FeedbackService.create_feedback(ticket_id, user_id, rating, comment)
