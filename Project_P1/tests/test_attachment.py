from io import BytesIO

from services.ticket_attachment_service import TicketAttachmentService


def test_invalid_file_type():

    result = TicketAttachmentService.is_allowed_file("malware.exe")

    assert result is False


def test_allowed_file_type():

    result = TicketAttachmentService.is_allowed_file("document.pdf")

    assert result is True
