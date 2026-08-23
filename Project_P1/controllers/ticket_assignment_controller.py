from services.ticket_assignment_service import TicketAssignmentService


class TicketAssignmentController:

    @staticmethod
    def assign_ticket(ticket_id, agent_id, assigned_by):
        return TicketAssignmentService.assign_ticket(ticket_id, agent_id, assigned_by)
