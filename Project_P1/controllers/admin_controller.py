from services.admin_service import AdminService


class AdminController:

    @staticmethod
    def get_dashboard_data():
        return AdminService.get_dashboard_data()

    @staticmethod
    def create_agent(name, email, password):

        if not name or not email or not password:
            return None, "All fields are required"

        if len(name.strip()) < 2:
            return None, "Name must contain at least 2 characters"

        if len(password) < 6:
            return None, "Password must contain at least 6 characters"

        return AdminService.create_agent(name, email, password)
