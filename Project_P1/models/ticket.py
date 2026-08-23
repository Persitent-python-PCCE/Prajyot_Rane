from extensions import db


class Ticket(db.Model):

    __tablename__ = "tickets"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)

    description = db.Column(db.Text, nullable=False)

    priority = db.Column(db.String(20), nullable=False, default="Medium")

    severity = db.Column(db.String(20), nullable=False, default="Medium")

    status = db.Column(db.String(20), nullable=False, default="Open")

    requester_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    category_id = db.Column(
        db.Integer, db.ForeignKey("ticket_categories.id"), nullable=False
    )

    response_due_at = db.Column(db.DateTime, nullable=True)

    resolution_due_at = db.Column(db.DateTime, nullable=True)

    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.func.now(),
        onupdate=db.func.now(),
    )

    requester = db.relationship("User", back_populates="tickets")

    category = db.relationship("TicketCategory", back_populates="tickets")

    comments = db.relationship(
        "TicketComment", back_populates="ticket", cascade="all, delete-orphan"
    )

    attachments = db.relationship(
        "TicketAttachment", back_populates="ticket", cascade="all, delete-orphan"
    )

    assignments = db.relationship(
        "TicketAssignment", back_populates="ticket", cascade="all, delete-orphan"
    )

    history = db.relationship(
        "TicketHistory", back_populates="ticket", cascade="all, delete-orphan"
    )

    feedback = db.relationship(
        "Feedback", back_populates="ticket", uselist=False, cascade="all, delete-orphan"
    )

    @property
    def current_assignment(self):

        if not self.assignments:
            return None

        return max(self.assignments, key=lambda assignment: assignment.assigned_at)
