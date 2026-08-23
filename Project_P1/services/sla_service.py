from datetime import datetime, timedelta

from dao.sla_rule_dao import SlaRuleDAO
from dao.ticket_dao import TicketDAO
from dao.ticket_history_dao import TicketHistoryDAO

from services.ticket_history_service import TicketHistoryService


class SlaService:

    @staticmethod
    def calculate_sla(priority, created_at=None):

        if not priority:
            return None, "Priority is required"

        rule = SlaRuleDAO.find_by_priority(priority)

        if not rule:
            return None, "No active SLA rule found for this priority"

        if created_at is None:
            created_at = datetime.now()

        response_due_at = created_at + timedelta(hours=rule.response_time_hours)

        resolution_due_at = created_at + timedelta(hours=rule.resolution_time_hours)

        return {
            "response_due_at": response_due_at,
            "resolution_due_at": resolution_due_at,
            "response_time_hours": rule.response_time_hours,
            "resolution_time_hours": rule.resolution_time_hours,
        }, None

    @staticmethod
    def get_breached_tickets():

        tickets = TicketDAO.find_sla_breaches()

        now = datetime.now()

        results = []

        for ticket in tickets:

            response_breached = (
                ticket.response_due_at is not None
                and now > ticket.response_due_at
                and ticket.status == "Open"
            )

            resolution_breached = (
                ticket.resolution_due_at is not None
                and now > ticket.resolution_due_at
                and ticket.status != "Closed"
            )

            if not response_breached and not resolution_breached:
                continue

            breach_type = []

            if response_breached:
                breach_type.append("Response SLA")

            if resolution_breached:
                breach_type.append("Resolution SLA")

            results.append({"ticket": ticket, "breach_type": breach_type})

        return results

    @staticmethod
    def record_breaches():

        breaches = SlaService.get_breached_tickets()

        recorded = []

        for item in breaches:

            ticket = item["ticket"]

            for breach_type in item["breach_type"]:

                action = f"{breach_type} Breached"

                already_recorded = TicketHistoryDAO.exists_for_action(ticket.id, action)

                if already_recorded:
                    continue

                TicketHistoryService.add_history(
                    ticket_id=ticket.id,
                    user_id=ticket.requester_id,
                    action=action,
                    old_value=None,
                    new_value="Escalated",
                )

                recorded.append({"ticket_id": ticket.id, "action": action})

        return recorded
