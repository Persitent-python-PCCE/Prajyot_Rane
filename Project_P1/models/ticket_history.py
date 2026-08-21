from extensions import db


class TicketHistory(db.Model):

    __tablename__ = "ticket_history"

    id = db.Column(db.Integer, primary_key=True)

    ticket_id = db.Column(db.Integer, db.ForeignKey("tickets.id"), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    action = db.Column(db.String(100), nullable=False)

    old_value = db.Column(db.Text, nullable=True)

    new_value = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    ticket = db.relationship("Ticket", back_populates="history")

    user = db.relationship("User", back_populates="history")
