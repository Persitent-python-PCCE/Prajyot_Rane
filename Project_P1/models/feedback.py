from extensions import db


class Feedback(db.Model):

    __tablename__ = "feedback"

    id = db.Column(db.Integer, primary_key=True)

    ticket_id = db.Column(
        db.Integer, db.ForeignKey("tickets.id"), nullable=False, unique=True
    )

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    rating = db.Column(db.Integer, nullable=False)

    comment = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    ticket = db.relationship("Ticket", back_populates="feedback")

    user = db.relationship("User", back_populates="feedback")
