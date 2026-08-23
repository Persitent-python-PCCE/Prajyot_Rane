import bcrypt

from models.user import User

from dao.admin_dao import AdminDAO


class AdminService:

    @staticmethod
    def get_dashboard_data():

        tickets = AdminDAO.get_all_tickets()
        agents = AdminDAO.get_support_agents()

        return tickets, agents

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

        return AdminDAO.find_tickets(
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

        status_counts = AdminDAO.get_ticket_status_counts()
        priority_counts = AdminDAO.get_ticket_priority_counts()
        category_counts = AdminDAO.get_ticket_category_counts()

        return {
            "status": {status: count for status, count in status_counts},
            "priority": {priority: count for priority, count in priority_counts},
            "category": {
                str(category_id): count for category_id, count in category_counts
            },
        }

    @staticmethod
    def create_agent(name, email, password):

        email = email.strip().lower()

        existing_user = AdminDAO.find_user_by_email(email)

        if existing_user:
            return None, "Email already registered"

        role = AdminDAO.get_role_by_name("SUPPORT_AGENT")

        if not role:
            return None, "Support Agent role not found"

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")

        agent = User(
            name=name.strip(),
            email=email,
            password=hashed_password,
            role_id=role.id,
            is_active=True,
        )

        AdminDAO.save_user(agent)

        return agent, None

    @staticmethod
    def get_all_users():

        return AdminDAO.get_all_users()

    @staticmethod
    def search_users(search=None, page=1, per_page=10):

        return AdminDAO.search_users(search=search, page=page, per_page=per_page)

    @staticmethod
    def set_user_status(user_id, is_active):

        user = AdminDAO.find_user_by_id(user_id)

        if not user:
            return None, "User not found"

        if user.role.name == "ADMIN":
            return None, "Admin accounts cannot be deactivated"

        user.is_active = is_active

        AdminDAO.update_user(user)

        return user, None
