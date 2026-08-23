from flask import Blueprint, request, redirect, url_for, session, jsonify

from utils.auth_decorators import login_required, login_required_api, get_api_user_id

from utils.ticket_access import ticket_access_required, ticket_access_required_api

from controllers.ticket_comment_controller import TicketCommentController

comment_bp = Blueprint("comment", __name__, url_prefix="/comment")


@comment_bp.route("/tickets/<int:ticket_id>", methods=["POST"])
@login_required
@ticket_access_required
def add_comment(ticket_id):

    comment = request.form.get("comment")

    if not comment or not comment.strip():
        return "Comment is required", 400

    new_comment, error = TicketCommentController.add_comment(
        ticket_id, session["user_id"], comment
    )

    if error:
        return error, 400

    return redirect(url_for("ticket.ticket_details", ticket_id=ticket_id))


@comment_bp.route("/api/tickets/<int:ticket_id>", methods=["POST"])
@login_required_api
@ticket_access_required_api
def api_add_comment(ticket_id):

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"success": False, "error": "Request body is required"}), 400

    comment = data.get("comment")

    if not comment or not comment.strip():
        return jsonify({"success": False, "error": "Comment is required"}), 400

    new_comment, error = TicketCommentController.add_comment(
        ticket_id, get_api_user_id(), comment
    )

    if error:
        return jsonify({"success": False, "error": error}), 400

    return (
        jsonify(
            {
                "success": True,
                "message": "Comment added successfully",
                "comment": {
                    "id": new_comment.id,
                    "ticket_id": new_comment.ticket_id,
                    "user_id": new_comment.user_id,
                    "comment": new_comment.comment,
                    "created_at": (
                        new_comment.created_at.isoformat()
                        if new_comment.created_at
                        else None
                    ),
                },
            }
        ),
        201,
    )
