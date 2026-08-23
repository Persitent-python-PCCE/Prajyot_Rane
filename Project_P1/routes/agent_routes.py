from flask import (
    Blueprint,
    request,
    redirect,
    url_for,
    session,
    jsonify,
    render_template,
)

from utils.auth_decorators import (
    login_required,
    role_required,
    role_required_api,
    get_api_user_id,
)

from controllers.ticket_assignment_controller import TicketAssignmentController

from controllers.ticket_status_controller import TicketStatusController

from controllers.agent_controller import AgentController

agent_bp = Blueprint("agent", __name__, url_prefix="/agent")


@agent_bp.route("/dashboard")
@login_required
@role_required("SUPPORT_AGENT")
def dashboard():

    try:
        page = int(request.args.get("page", 1))
    except (TypeError, ValueError):
        page = 1

    if page < 1:
        page = 1

    pagination = AgentController.get_assigned_tickets(
        session["user_id"], page=page, per_page=10
    )

    return render_template(
        "agent_dashboard.html", assignments=pagination.items, pagination=pagination
    )


@agent_bp.route("/tickets/<int:ticket_id>/assign", methods=["POST"])
@role_required("ADMIN")
def assign_ticket(ticket_id):

    agent_id = request.form.get("agent_id")

    if not agent_id:
        return "Agent ID is required", 400

    assignment, error = TicketAssignmentController.assign_ticket(
        ticket_id=ticket_id, agent_id=agent_id, assigned_by=session["user_id"]
    )

    if error:
        return error, 400

    return redirect(url_for("ticket.ticket_details", ticket_id=ticket_id))


@agent_bp.route("/tickets/<int:ticket_id>/status", methods=["POST"])
@role_required("SUPPORT_AGENT", "ADMIN")
def change_status(ticket_id):

    new_status = request.form.get("status")

    if not new_status:
        return "Status is required", 400

    ticket, error = TicketStatusController.change_status(
        ticket_id=ticket_id, new_status=new_status, user_id=session["user_id"]
    )

    if error:
        return error, 400

    return redirect(url_for("ticket.ticket_details", ticket_id=ticket_id))


@agent_bp.route("/api/tickets/<int:ticket_id>/status", methods=["PUT"])
@role_required_api("SUPPORT_AGENT", "ADMIN")
def api_change_status(ticket_id):

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"success": False, "error": "Request body is required"}), 400

    new_status = data.get("status")

    if not new_status:
        return jsonify({"success": False, "error": "Status is required"}), 400

    ticket, error = TicketStatusController.change_status(
        ticket_id=ticket_id, new_status=new_status, user_id=get_api_user_id()
    )

    if error:
        return jsonify({"success": False, "error": error}), 400

    return (
        jsonify(
            {
                "success": True,
                "message": "Ticket status updated successfully",
                "ticket": {"id": ticket.id, "status": ticket.status},
            }
        ),
        200,
    )


@agent_bp.route("/api/tickets/<int:ticket_id>/assign", methods=["POST"])
@role_required_api("ADMIN")
def api_assign_ticket(ticket_id):

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"success": False, "error": "Request body is required"}), 400

    agent_id = data.get("agent_id")

    if not agent_id:
        return jsonify({"success": False, "error": "agent_id is required"}), 400

    assignment, error = TicketAssignmentController.assign_ticket(
        ticket_id=ticket_id, agent_id=agent_id, assigned_by=get_api_user_id()
    )

    if error:
        return jsonify({"success": False, "error": error}), 400

    return (
        jsonify(
            {
                "success": True,
                "message": "Ticket assigned successfully",
                "assignment": {
                    "id": assignment.id,
                    "ticket_id": assignment.ticket_id,
                    "agent_id": assignment.agent_id,
                    "assigned_by": assignment.assigned_by,
                    "assigned_at": (
                        assignment.assigned_at.isoformat()
                        if assignment.assigned_at
                        else None
                    ),
                },
            }
        ),
        201,
    )


@agent_bp.route("/api/tickets", methods=["GET"])
@role_required_api("SUPPORT_AGENT")
def api_assigned_tickets():

    try:
        page = int(request.args.get("page", 1))
    except (TypeError, ValueError):
        page = 1

    if page < 1:
        page = 1

    pagination = AgentController.get_assigned_tickets(
        get_api_user_id(), page=page, per_page=10
    )

    return (
        jsonify(
            {
                "success": True,
                "page": pagination.page,
                "per_page": pagination.per_page,
                "total": pagination.total,
                "pages": pagination.pages,
                "tickets": [
                    {
                        "assignment_id": assignment.id,
                        "ticket_id": assignment.ticket.id,
                        "title": assignment.ticket.title,
                        "description": assignment.ticket.description,
                        "status": assignment.ticket.status,
                        "priority": assignment.ticket.priority,
                        "severity": assignment.ticket.severity,
                        "category": assignment.ticket.category.name,
                        "requester_id": assignment.ticket.requester_id,
                        "assigned_at": (
                            assignment.assigned_at.isoformat()
                            if assignment.assigned_at
                            else None
                        ),
                        "response_due_at": (
                            assignment.ticket.response_due_at.isoformat()
                            if assignment.ticket.response_due_at
                            else None
                        ),
                        "resolution_due_at": (
                            assignment.ticket.resolution_due_at.isoformat()
                            if assignment.ticket.resolution_due_at
                            else None
                        ),
                    }
                    for assignment in pagination.items
                ],
            }
        ),
        200,
    )
