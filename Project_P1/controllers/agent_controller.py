from services.agent_service import AgentService


class AgentController:

    @staticmethod
    def get_assigned_tickets(agent_id, page=1, per_page=10):
        return AgentService.get_assigned_tickets(agent_id, page=page, per_page=per_page)
