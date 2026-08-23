from dao.ticket_assignment_dao import TicketAssignmentDAO


class AgentService:

    @staticmethod
    def get_assigned_tickets(agent_id, page=1, per_page=10):
        return TicketAssignmentDAO.find_by_agent(agent_id, page=page, per_page=per_page)
