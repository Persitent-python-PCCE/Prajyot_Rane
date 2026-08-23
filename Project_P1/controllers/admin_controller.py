from services.admin_service import AdminService


class AdminController:

    @staticmethod
    def get_dashboard_data():
        return AdminService.get_dashboard_data()

    @staticmethod
    def search_tickets(
        status=None,
        priority=None,
        severity=None,
        category_id=None,
        requester_id=None,
        agent_id=None,
        page=1,
        per_page=10,
    ):
        return AdminService.search_tickets(
            status=status,
            priority=priority,
            severity=severity,
            category_id=category_id,
            requester_id=requester_id,
            agent_id=agent_id,
            page=page,
            per_page=per_page,
        )

    @staticmethod
    def get_reports():
        return AdminService.get_reports()

    @staticmethod
    def create_agent(name, email, password):

        if not name or not email or not password:
            return None, "All fields are required"

        if len(name.strip()) < 2:
            return None, "Name must contain at least 2 characters"

        if len(password) < 6:
            return None, "Password must contain at least 6 characters"

        return AdminService.create_agent(name, email, password)

    @staticmethod
    def get_all_users():
        return AdminService.get_all_users()

    @staticmethod
    def search_users(search=None, page=1, per_page=10):
        return AdminService.search_users(search=search, page=page, per_page=per_page)

    @staticmethod
    def set_user_status(user_id, is_active):
        return AdminService.set_user_status(user_id, is_active)
