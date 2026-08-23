from extensions import db
from models.feedback import Feedback
from models.ticket import Ticket
from models.user import User
from services.feedback_service import FeedbackService


def test_create_feedback(app):

    with app.app_context():

        ticket = db.session.get(Ticket, 1)
        assert ticket is not None

        user = db.session.get(User, ticket.requester_id)
        assert user is not None

        existing = Feedback.query.filter_by(
            ticket_id=ticket.id, user_id=user.id
        ).first()

        if existing:
            db.session.delete(existing)
            db.session.commit()

        feedback, error = FeedbackService.create_feedback(
            ticket_id=ticket.id, user_id=user.id, rating=5, comment="Good service"
        )

        assert error is None
        assert feedback is not None
        assert feedback.ticket_id == ticket.id
        assert feedback.user_id == user.id
        assert feedback.rating == 5

        db.session.delete(feedback)
        db.session.commit()
