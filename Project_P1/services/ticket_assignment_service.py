from models.ticket_assignment import TicketAssignment

from dao.ticket_assignment_dao import TicketAssignmentDAO
from dao.ticket_dao import TicketDAO
from dao.user_dao import UserDAO

from services.ticket_history_service import TicketHistoryService


class TicketAssignmentService:

    @staticmethod
    def assign_ticket(ticket_id, agent_id, assigned_by):

        ticket = TicketDAO.find_by_id(ticket_id)

        if not ticket:
            return None, "Ticket not found"

        agent = UserDAO.find_by_id(agent_id)

        if not agent:
            return None, "Agent not found"

        if not agent.role:
            return None, "User role not found"

        if agent.role.name != "SUPPORT_AGENT":
            return None, "Selected user is not a support agent"

        if not agent.is_active:
            return None, "Selected support agent is inactive"

        current_assignment = TicketAssignmentDAO.find_current_assignment(ticket_id)

        if current_assignment:
            if current_assignment.agent_id == agent_id:
                return None, "Ticket is already assigned to this agent"

        assignment = TicketAssignment(
            ticket_id=ticket_id, agent_id=agent_id, assigned_by=assigned_by
        )

        TicketAssignmentDAO.save(assignment)

        old_status = ticket.status

        ticket.status = "Assigned"

        TicketDAO.update(ticket)

        TicketHistoryService.add_history(
            ticket_id=ticket_id,
            user_id=assigned_by,
            action="Ticket Assigned",
            old_value=old_status,
            new_value=f"Assigned to {agent.name}",
        )

        return assignment, None
