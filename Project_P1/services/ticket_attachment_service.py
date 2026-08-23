import os
import uuid

from flask import current_app
from werkzeug.utils import secure_filename

from models.ticket_attachment import TicketAttachment

from dao.ticket_attachment_dao import TicketAttachmentDAO
from dao.ticket_dao import TicketDAO

ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg",
    "gif",
    "pdf",
    "txt",
    "log",
    "csv",
    "doc",
    "docx",
    "xls",
    "xlsx",
}

MAX_FILE_SIZE = 5 * 1024 * 1024


class TicketAttachmentService:

    @staticmethod
    def is_allowed_file(filename):

        if not filename or "." not in filename:
            return False

        extension = filename.rsplit(".", 1)[1].lower()

        return extension in ALLOWED_EXTENSIONS

    @staticmethod
    def get_file_size(file):

        current_position = file.tell()

        file.seek(0, os.SEEK_END)

        file_size = file.tell()

        file.seek(current_position)

        return file_size

    @staticmethod
    def upload_attachment(ticket_id, uploaded_by, file):

        ticket = TicketDAO.find_by_id(ticket_id)

        if not ticket:
            return None, "Ticket not found"

        if not file:
            return None, "File is required"

        if not file.filename:
            return None, "No file selected"

        if not TicketAttachmentService.is_allowed_file(file.filename):
            return None, "File type is not allowed"

        file_size = TicketAttachmentService.get_file_size(file)

        if file_size > MAX_FILE_SIZE:
            return None, "File size cannot exceed 5 MB"

        original_filename = secure_filename(file.filename)

        if not original_filename:
            return None, "Invalid filename"

        extension = ""

        if "." in original_filename:
            extension = "." + original_filename.rsplit(".", 1)[1].lower()

        stored_filename = str(uuid.uuid4()) + extension

        upload_folder = current_app.config.get("UPLOAD_FOLDER", "uploads")

        os.makedirs(upload_folder, exist_ok=True)

        file_path = os.path.join(upload_folder, stored_filename)

        try:
            file.save(file_path)

            attachment = TicketAttachment(
                ticket_id=ticket_id,
                uploaded_by=uploaded_by,
                filename=original_filename,
                filepath=file_path,
                file_size=file_size,
            )

            TicketAttachmentDAO.save(attachment)

            return attachment, None

        except Exception as error:

            if os.path.exists(file_path):
                os.remove(file_path)

            return None, "Failed to upload file"

    @staticmethod
    def get_ticket_attachments(ticket_id):

        return TicketAttachmentDAO.find_by_ticket(ticket_id)

    @staticmethod
    def get_attachment(attachment_id):

        return TicketAttachmentDAO.find_by_id(attachment_id)
