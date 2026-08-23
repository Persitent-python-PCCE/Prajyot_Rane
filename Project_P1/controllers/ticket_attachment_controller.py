from services.ticket_attachment_service import TicketAttachmentService


class TicketAttachmentController:

    @staticmethod
    def upload_attachment(ticket_id, uploaded_by, file):

        if not file:
            return None, "File is required"

        return TicketAttachmentService.upload_attachment(ticket_id, uploaded_by, file)

    @staticmethod
    def get_ticket_attachments(ticket_id):

        return TicketAttachmentService.get_ticket_attachments(ticket_id)

    @staticmethod
    def get_attachment(attachment_id):

        return TicketAttachmentService.get_attachment(attachment_id)
