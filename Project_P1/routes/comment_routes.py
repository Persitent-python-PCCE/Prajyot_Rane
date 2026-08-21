from flask import Blueprint, request, redirect, url_for, session

from controllers.ticket_comment_controller import TicketCommentController

comment_bp = Blueprint("comment", __name__, url_prefix="/tickets")


@comment_bp.route("/<int:ticket_id>/comments", methods=["POST"])
def add_comment(ticket_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    comment_text = request.form.get("comment")

    comment, error = TicketCommentController.add_comment(
        ticket_id, session["user_id"], comment_text
    )

    if error:
        return error, 400

    return redirect(url_for("ticket.ticket_details", ticket_id=ticket_id))
