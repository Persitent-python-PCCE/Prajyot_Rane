from extensions import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(150), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)

    role = db.relationship("Role", back_populates="users")

    tickets = db.relationship("Ticket", back_populates="requester")

    comments = db.relationship("TicketComment", back_populates="user")

    attachments = db.relationship("TicketAttachment", back_populates="user")

    assigned_tickets = db.relationship(
        "TicketAssignment",
        foreign_keys="TicketAssignment.agent_id",
        back_populates="agent",
    )

    created_assignments = db.relationship(
        "TicketAssignment",
        foreign_keys="TicketAssignment.assigned_by",
        back_populates="assigner",
    )

    history = db.relationship("TicketHistory", back_populates="user")

    feedback = db.relationship("Feedback", back_populates="user")

    is_active = db.Column(db.Boolean, nullable=False, default=True)
