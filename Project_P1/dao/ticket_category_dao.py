from models.ticket_category import TicketCategory
from extensions import db


class TicketCategoryDAO:

    @staticmethod
    def find_by_id(category_id):
        return db.session.get(TicketCategory, category_id)

    @staticmethod
    def get_all():
        return TicketCategory.query.order_by(TicketCategory.name).all()


def test_invalid_ticket_status_transition(client):

    login_response = client.post(
        "/auth/api/login", json={"email": "user4@email.com", "password": "123456"}
    )

    assert login_response.status_code == 200

    token = login_response.get_json()["access_token"]

    response = client.put(
        "/agent/api/tickets/1/status",
        headers={"Authorization": f"Bearer {token}"},
        json={"status": "Closed"},
    )

    assert response.status_code in [400, 403]

    data = response.get_json()

    assert data["success"] is False
