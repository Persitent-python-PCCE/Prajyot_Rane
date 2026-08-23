from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    jsonify,
)

from utils.auth_decorators import login_required, login_required_api, get_api_user_id

from utils.ticket_access import ticket_access_required, ticket_access_required_api

from dao.ticket_category_dao import TicketCategoryDAO

from controllers.ticket_controller import TicketController

ticket_bp = Blueprint("ticket", __name__, url_prefix="/tickets")


@ticket_bp.route("/create", methods=["GET", "POST"])
@login_required
def create_ticket():

    categories = TicketCategoryDAO.get_all()

    if request.method == "GET":
        return render_template("create_ticket.html", categories=categories)

    title = request.form.get("title")
    description = request.form.get("description")
    priority = request.form.get("priority")
    severity = request.form.get("severity")
    category_id = request.form.get("category_id")

    ticket, error = TicketController.create_ticket(
        title, description, priority, severity, category_id, session["user_id"]
    )

    if error:
        return render_template("create_ticket.html", categories=categories, error=error)

    return redirect(url_for("ticket.ticket_details", ticket_id=ticket.id))


@ticket_bp.route("/my-tickets")
@login_required
def my_tickets():

    try:
        page = int(request.args.get("page", 1))
    except (TypeError, ValueError):
        page = 1

    if page < 1:
        page = 1

    pagination = TicketController.get_user_tickets(
        session["user_id"], page=page, per_page=10
    )

    return render_template(
        "my_tickets.html", tickets=pagination.items, pagination=pagination
    )


@ticket_bp.route("/<int:ticket_id>")
@login_required
@ticket_access_required
def ticket_details(ticket_id):

    ticket = TicketController.get_ticket(ticket_id)

    if not ticket:
        return "Ticket not found", 404

    return render_template("ticket_details.html", ticket=ticket)


@ticket_bp.route("/api/create", methods=["POST"])
@login_required_api
def api_create_ticket():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"success": False, "error": "Request body is required"}), 400

    title = data.get("title")
    description = data.get("description")
    priority = data.get("priority")
    severity = data.get("severity")
    category_id = data.get("category_id")

    ticket, error = TicketController.create_ticket(
        title, description, priority, severity, category_id, get_api_user_id()
    )

    if error:
        return jsonify({"success": False, "error": error}), 400

    return (
        jsonify(
            {
                "success": True,
                "message": "Ticket created successfully",
                "ticket": {
                    "id": ticket.id,
                    "title": ticket.title,
                    "description": ticket.description,
                    "status": ticket.status,
                    "priority": ticket.priority,
                    "severity": ticket.severity,
                    "category_id": ticket.category_id,
                    "requester_id": ticket.requester_id,
                    "response_due_at": (
                        ticket.response_due_at.isoformat()
                        if ticket.response_due_at
                        else None
                    ),
                    "resolution_due_at": (
                        ticket.resolution_due_at.isoformat()
                        if ticket.resolution_due_at
                        else None
                    ),
                },
            }
        ),
        201,
    )


@ticket_bp.route("/api/my-tickets", methods=["GET"])
@login_required_api
def api_my_tickets():

    try:
        page = int(request.args.get("page", 1))
    except (TypeError, ValueError):
        page = 1

    if page < 1:
        page = 1

    pagination = TicketController.get_user_tickets(
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
                        "id": ticket.id,
                        "title": ticket.title,
                        "status": ticket.status,
                        "priority": ticket.priority,
                        "severity": ticket.severity,
                        "category": ticket.category.name,
                        "created_at": (
                            ticket.created_at.isoformat() if ticket.created_at else None
                        ),
                        "response_due_at": (
                            ticket.response_due_at.isoformat()
                            if ticket.response_due_at
                            else None
                        ),
                        "resolution_due_at": (
                            ticket.resolution_due_at.isoformat()
                            if ticket.resolution_due_at
                            else None
                        ),
                    }
                    for ticket in pagination.items
                ],
            }
        ),
        200,
    )


@ticket_bp.route("/api/<int:ticket_id>", methods=["GET"])
@login_required_api
@ticket_access_required_api
def api_ticket_details(ticket_id):

    ticket = TicketController.get_ticket(ticket_id)

    if not ticket:
        return jsonify({"success": False, "error": "Ticket not found"}), 404

    return (
        jsonify(
            {
                "success": True,
                "ticket": {
                    "id": ticket.id,
                    "title": ticket.title,
                    "description": ticket.description,
                    "status": ticket.status,
                    "priority": ticket.priority,
                    "severity": ticket.severity,
                    "category": ticket.category.name,
                    "requester_id": ticket.requester_id,
                    "created_at": (
                        ticket.created_at.isoformat() if ticket.created_at else None
                    ),
                    "updated_at": (
                        ticket.updated_at.isoformat() if ticket.updated_at else None
                    ),
                    "response_due_at": (
                        ticket.response_due_at.isoformat()
                        if ticket.response_due_at
                        else None
                    ),
                    "resolution_due_at": (
                        ticket.resolution_due_at.isoformat()
                        if ticket.resolution_due_at
                        else None
                    ),
                    "assigned_agent_id": (
                        ticket.current_assignment.agent_id
                        if ticket.current_assignment
                        else None
                    ),
                },
            }
        ),
        200,
    )
