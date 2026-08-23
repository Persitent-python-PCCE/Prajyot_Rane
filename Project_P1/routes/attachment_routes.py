from flask import Blueprint, request, redirect, url_for, session, send_file, jsonify

from flask_jwt_extended import get_jwt

from controllers.ticket_attachment_controller import TicketAttachmentController

from dao.ticket_dao import TicketDAO

from utils.auth_decorators import login_required, login_required_api, get_api_user_id

from utils.ticket_access import ticket_access_required, ticket_access_required_api

attachment_bp = Blueprint("attachment", __name__, url_prefix="/tickets")


@attachment_bp.route("/<int:ticket_id>/attachments", methods=["POST"])
@login_required
@ticket_access_required
def upload_attachment(ticket_id):

    file = request.files.get("file")

    if not file:
        return "File is required", 400

    attachment, error = TicketAttachmentController.upload_attachment(
        ticket_id, session["user_id"], file
    )

    if error:
        return error, 400

    return redirect(url_for("ticket.ticket_details", ticket_id=ticket_id))


@attachment_bp.route("/attachments/<int:attachment_id>/download", methods=["GET"])
@login_required
def download_attachment(attachment_id):

    attachment = TicketAttachmentController.get_attachment(attachment_id)

    if not attachment:
        return "Attachment not found", 404

    ticket = TicketDAO.find_by_id(attachment.ticket_id)

    if not ticket:
        return "Ticket not found", 404

    user_id = session["user_id"]
    role = session["role"]

    if role == "EMPLOYEE":

        if ticket.requester_id != user_id:
            return "Unauthorized", 403

    elif role == "SUPPORT_AGENT":

        assigned = any(
            assignment.agent_id == user_id for assignment in ticket.assignments
        )

        if not assigned:
            return "Unauthorized", 403

    elif role != "ADMIN":

        return "Unauthorized", 403

    return send_file(
        attachment.filepath, as_attachment=True, download_name=attachment.filename
    )


@attachment_bp.route("/api/<int:ticket_id>/attachments", methods=["POST"])
@login_required_api
@ticket_access_required_api
def api_upload_attachment(ticket_id):

    file = request.files.get("file")

    if not file:
        return jsonify({"success": False, "error": "File is required"}), 400

    attachment, error = TicketAttachmentController.upload_attachment(
        ticket_id, get_api_user_id(), file
    )

    if error:
        return jsonify({"success": False, "error": error}), 400

    return (
        jsonify(
            {
                "success": True,
                "message": "File uploaded successfully",
                "attachment": {
                    "id": attachment.id,
                    "ticket_id": attachment.ticket_id,
                    "filename": attachment.filename,
                    "file_size": attachment.file_size,
                    "uploaded_by": attachment.uploaded_by,
                    "uploaded_at": (
                        attachment.uploaded_at.isoformat()
                        if attachment.uploaded_at
                        else None
                    ),
                },
            }
        ),
        201,
    )


@attachment_bp.route("/api/<int:ticket_id>/attachments", methods=["GET"])
@login_required_api
@ticket_access_required_api
def api_get_ticket_attachments(ticket_id):

    attachments = TicketAttachmentController.get_ticket_attachments(ticket_id)

    return (
        jsonify(
            {
                "success": True,
                "ticket_id": ticket_id,
                "count": len(attachments),
                "attachments": [
                    {
                        "id": attachment.id,
                        "ticket_id": attachment.ticket_id,
                        "filename": attachment.filename,
                        "file_size": attachment.file_size,
                        "uploaded_by": attachment.uploaded_by,
                        "uploaded_at": (
                            attachment.uploaded_at.isoformat()
                            if attachment.uploaded_at
                            else None
                        ),
                        "download_url": url_for(
                            "attachment.api_download_attachment",
                            attachment_id=attachment.id,
                            _external=True,
                        ),
                    }
                    for attachment in attachments
                ],
            }
        ),
        200,
    )


@attachment_bp.route("/api/attachments/<int:attachment_id>/download", methods=["GET"])
@login_required_api
def api_download_attachment(attachment_id):

    attachment = TicketAttachmentController.get_attachment(attachment_id)

    if not attachment:
        return jsonify({"success": False, "error": "Attachment not found"}), 404

    ticket = TicketDAO.find_by_id(attachment.ticket_id)

    if not ticket:
        return jsonify({"success": False, "error": "Ticket not found"}), 404

    user_id = get_api_user_id()
    role = get_jwt().get("role")

    if role == "EMPLOYEE":

        if ticket.requester_id != user_id:
            return jsonify({"success": False, "error": "Unauthorized"}), 403

    elif role == "SUPPORT_AGENT":

        assigned = any(
            assignment.agent_id == user_id for assignment in ticket.assignments
        )

        if not assigned:
            return jsonify({"success": False, "error": "Unauthorized"}), 403

    elif role != "ADMIN":

        return jsonify({"success": False, "error": "Unauthorized"}), 403

    return send_file(
        attachment.filepath, as_attachment=True, download_name=attachment.filename
    )
