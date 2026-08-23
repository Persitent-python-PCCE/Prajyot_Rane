from extensions import db
from models.ticket_attachment import TicketAttachment


class TicketAttachmentDAO:

    @staticmethod
    def save(attachment):
        db.session.add(attachment)
        db.session.commit()
        return attachment

    @staticmethod
    def find_by_id(attachment_id):
        return TicketAttachment.query.get(attachment_id)

    @staticmethod
    def find_by_ticket(ticket_id):
        return (
            TicketAttachment.query.filter_by(ticket_id=ticket_id)
            .order_by(TicketAttachment.uploaded_at.desc())
            .all()
        )
