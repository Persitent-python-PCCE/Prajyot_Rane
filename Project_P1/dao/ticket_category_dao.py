from models.ticket_category import TicketCategory


class TicketCategoryDAO:

    @staticmethod
    def find_by_id(category_id):
        return TicketCategory.query.get(category_id)

    @staticmethod
    def get_all():
        return TicketCategory.query.order_by(TicketCategory.name).all()
