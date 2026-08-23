from extensions import db
from models.feedback import Feedback


class FeedbackDAO:

    @staticmethod
    def save(feedback):
        db.session.add(feedback)
        db.session.commit()
        return feedback

    @staticmethod
    def find_by_ticket(ticket_id):
        return Feedback.query.filter_by(ticket_id=ticket_id).first()

    @staticmethod
    def find_by_user(user_id):
        return (
            Feedback.query.filter_by(user_id=user_id)
            .order_by(Feedback.created_at.desc())
            .all()
        )

    @staticmethod
    def get_all():
        return Feedback.query.order_by(Feedback.created_at.desc()).all()
