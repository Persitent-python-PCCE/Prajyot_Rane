from extensions import db


class TicketAssignment(db.Model):

    __tablename__ = "ticket_assignments"
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey("tickets.id"), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    assigned_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    assigned_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    ticket = db.relationship("Ticket", back_populates="assignments")
    agent = db.relationship(
        "User", foreign_keys=[agent_id], back_populates="assigned_tickets"
    )
    assigner = db.relationship(
        "User", foreign_keys=[assigned_by], back_populates="created_assignments"
    )
