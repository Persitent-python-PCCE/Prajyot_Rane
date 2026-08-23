from extensions import db
from models.user import User


class UserDAO:

    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def find_by_id(user_id):
        return db.session.get(User, user_id)

    @staticmethod
    def save(user):
        db.session.add(user)
        db.session.commit()
        return user
