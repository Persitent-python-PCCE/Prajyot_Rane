from services.sla_service import SlaService


def test_calculate_sla(app):

    with app.app_context():

        result, error = SlaService.calculate_sla("High")

        assert error is None
        assert result is not None
        assert result["response_time_hours"] == 2
        assert result["resolution_time_hours"] == 8
        assert result["response_due_at"] is not None
        assert result["resolution_due_at"] is not None


def test_calculate_sla_invalid_priority(app):

    with app.app_context():

        result, error = SlaService.calculate_sla("InvalidPriority")

        assert result is None
        assert error == "No active SLA rule found for this priority"
