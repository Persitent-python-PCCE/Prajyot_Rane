from models.sla_rule import SlaRule


class SlaRuleDAO:

    @staticmethod
    def find_by_priority(priority):
        return SlaRule.query.filter_by(priority=priority, is_active=True).first()

    @staticmethod
    def get_all():
        return SlaRule.query.order_by(SlaRule.priority).all()
