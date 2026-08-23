from services.sla_service import SlaService


class SlaController:

    @staticmethod
    def calculate_sla(priority, created_at=None):
        return SlaService.calculate_sla(priority, created_at)

    @staticmethod
    def get_breached_tickets():
        return SlaService.get_breached_tickets()

    @staticmethod
    def record_breaches():
        return SlaService.record_breaches()
