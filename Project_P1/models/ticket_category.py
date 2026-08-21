from extensions import db


class TicketCategory(db.Model):
    __tablename__ = "ticket_categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    tickets = db.relationship("Ticket", back_populates="category")
