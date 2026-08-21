from models.roles import Role


class RoleDAO:

    @staticmethod
    def find_by_name(name):
        return Role.query.filter_by(name=name).first()

    @staticmethod
    def find_by_id(role_id):
        return Role.query.get(role_id)

    @staticmethod
    def get_all():
        return Role.query.all()
