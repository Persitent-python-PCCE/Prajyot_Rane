from extensions import db
from models.ticket import Ticket
from models.user import User
from models.roles import Role
from models.ticket_category import TicketCategory
from services.ticket_assignment_service import TicketAssignmentService


def test_assign_ticket(app):

    with app.app_context():

        category = TicketCategory.query.first()
        assert category is not None

        employee_role = Role.query.filter_by(name="EMPLOYEE").first()

        assert employee_role is not None

        employee = User.query.filter_by(
            role_id=employee_role.id, is_active=True
        ).first()

        assert employee is not None

        agent_role = Role.query.filter_by(name="SUPPORT_AGENT").first()

        assert agent_role is not None

        agent = User.query.filter_by(role_id=agent_role.id, is_active=True).first()

        assert agent is not None

        ticket = Ticket(
            title="Assignment Test Ticket",
            description="Testing ticket assignment",
            priority="Medium",
            severity="Medium",
            status="Open",
            requester_id=employee.id,
            category_id=category.id,
        )

        db.session.add(ticket)
        db.session.commit()

        assignment, error = TicketAssignmentService.assign_ticket(
            ticket_id=ticket.id, agent_id=agent.id, assigned_by=employee.id
        )

        assert error is None
        assert assignment is not None
        assert assignment.ticket_id == ticket.id
        assert assignment.agent_id == agent.id

        db.session.delete(ticket)
        db.session.commit()
