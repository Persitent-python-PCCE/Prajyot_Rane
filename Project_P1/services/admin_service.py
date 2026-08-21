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
            name=name.strip(), email=email, password=hashed_password, role_id=role.id
        )

        AdminDAO.save_user(agent)

        return agent, None
