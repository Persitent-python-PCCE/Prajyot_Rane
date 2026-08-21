from flask import Blueprint, request, redirect, url_for, session

from controllers.auth_controller import AuthController

from controllers.ticket_assignment_controller import TicketAssignmentController

from controllers.ticket_status_controller import TicketStatusController

agent_bp = Blueprint("agent", __name__, url_prefix="/agent")


@agent_bp.route("/tickets/<int:ticket_id>/assign", methods=["POST"])
def assign_ticket(ticket_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if not AuthController.has_role(["ADMIN"], session.get("role")):
        return "Unauthorized", 403

    agent_id = request.form.get("agent_id")

    assignment, error = TicketAssignmentController.assign_ticket(
        ticket_id=ticket_id, agent_id=agent_id, assigned_by=session["user_id"]
    )

    if error:
        return error, 400

    return redirect(url_for("ticket.ticket_details", ticket_id=ticket_id))


@agent_bp.route("/tickets/<int:ticket_id>/status", methods=["POST"])
def change_status(ticket_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if not AuthController.has_role(["SUPPORT_AGENT", "ADMIN"], session.get("role")):
        return "Unauthorized", 403

    new_status = request.form.get("status")

    ticket, error = TicketStatusController.change_status(
        ticket_id=ticket_id, new_status=new_status, user_id=session["user_id"]
    )

    if error:
        return error, 400

    return redirect(url_for("ticket.ticket_details", ticket_id=ticket_id))
