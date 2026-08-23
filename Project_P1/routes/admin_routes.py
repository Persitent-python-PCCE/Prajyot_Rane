from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    jsonify,
)

from dao.ticket_category_dao import TicketCategoryDAO

from utils.auth_decorators import (
    role_required,
    role_required_api,
)

from controllers.admin_controller import AdminController
from controllers.sla_controller import SlaController

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/dashboard")
@role_required("ADMIN")
def dashboard():

    status = request.args.get("status")
    priority = request.args.get("priority")
    severity = request.args.get("severity")
    category_id = request.args.get("category_id")
    agent_id = request.args.get("agent_id")

    try:
        page = int(request.args.get("page", 1))
    except (TypeError, ValueError):
        page = 1

    if page < 1:
        page = 1

    if category_id:
        try:
            category_id = int(category_id)
        except ValueError:
            category_id = None

    if agent_id:
        try:
            agent_id = int(agent_id)
        except ValueError:
            agent_id = None

    pagination = AdminController.search_tickets(
        status=status,
        priority=priority,
        severity=severity,
        category_id=category_id,
        agent_id=agent_id,
        page=page,
        per_page=10,
    )

    _, agents = AdminController.get_dashboard_data()

    reports = AdminController.get_reports()

    breaches = SlaController.get_breached_tickets()

    categories = TicketCategoryDAO.get_all()

    return render_template(
        "admin_dashboard.html",
        tickets=pagination.items,
        pagination=pagination,
        agents=agents,
        reports=reports,
        breaches=breaches,
        categories=categories,
    )


@admin_bp.route("/agents/create", methods=["GET", "POST"])
@role_required("ADMIN")
def create_agent():

    if request.method == "GET":
        return render_template("create_agent.html")

    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    agent, error = AdminController.create_agent(name, email, password)

    if error:
        return render_template("create_agent.html", error=error)

    return redirect(url_for("admin.dashboard"))


@admin_bp.route("/users")
@role_required("ADMIN")
def users():

    search = request.args.get("search", "").strip()

    try:
        page = int(request.args.get("page", 1))
    except (TypeError, ValueError):
        page = 1

    if page < 1:
        page = 1

    pagination = AdminController.search_users(search=search, page=page, per_page=10)

    return render_template(
        "admin_users.html", users=pagination.items, pagination=pagination, search=search
    )


@admin_bp.route("/users/<int:user_id>/status", methods=["POST"])
@role_required("ADMIN")
def change_user_status(user_id):

    is_active = request.form.get("is_active") == "true"

    user, error = AdminController.set_user_status(user_id, is_active)

    if error:
        return error, 400

    return redirect(url_for("admin.users"))


@admin_bp.route("/api/sla/breaches", methods=["GET"])
@role_required_api("ADMIN")
def api_sla_breaches():

    breaches = SlaController.get_breached_tickets()

    return (
        jsonify(
            {
                "success": True,
                "count": len(breaches),
                "breaches": [
                    {
                        "ticket_id": item["ticket"].id,
                        "title": item["ticket"].title,
                        "status": item["ticket"].status,
                        "priority": item["ticket"].priority,
                        "severity": item["ticket"].severity,
                        "requester_id": item["ticket"].requester_id,
                        "response_due_at": (
                            item["ticket"].response_due_at.isoformat()
                            if item["ticket"].response_due_at
                            else None
                        ),
                        "resolution_due_at": (
                            item["ticket"].resolution_due_at.isoformat()
                            if item["ticket"].resolution_due_at
                            else None
                        ),
                        "breach_type": item["breach_type"],
                    }
                    for item in breaches
                ],
            }
        ),
        200,
    )


@admin_bp.route("/api/sla/escalate", methods=["POST"])
@role_required_api("ADMIN")
def api_escalate_sla():

    recorded = SlaController.record_breaches()

    return (
        jsonify(
            {
                "success": True,
                "message": "SLA breaches processed successfully",
                "count": len(recorded),
                "escalations": recorded,
            }
        ),
        200,
    )


@admin_bp.route("/api/tickets", methods=["GET"])
@role_required_api("ADMIN")
def api_search_tickets():

    status = request.args.get("status")
    priority = request.args.get("priority")
    severity = request.args.get("severity")
    category_id = request.args.get("category_id")
    requester_id = request.args.get("requester_id")
    agent_id = request.args.get("agent_id")

    try:
        page = int(request.args.get("page", 1))
    except (TypeError, ValueError):
        page = 1

    if page < 1:
        page = 1

    if category_id:
        try:
            category_id = int(category_id)
        except ValueError:
            category_id = None

    if requester_id:
        try:
            requester_id = int(requester_id)
        except ValueError:
            requester_id = None

    if agent_id:
        try:
            agent_id = int(agent_id)
        except ValueError:
            agent_id = None

    pagination = AdminController.search_tickets(
        status=status,
        priority=priority,
        severity=severity,
        category_id=category_id,
        requester_id=requester_id,
        agent_id=agent_id,
        page=page,
        per_page=10,
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
                        "description": ticket.description,
                        "status": ticket.status,
                        "priority": ticket.priority,
                        "severity": ticket.severity,
                        "category_id": ticket.category_id,
                        "requester_id": ticket.requester_id,
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
                        "assigned_agent_id": (
                            ticket.current_assignment.agent_id
                            if ticket.current_assignment
                            else None
                        ),
                    }
                    for ticket in pagination.items
                ],
            }
        ),
        200,
    )


@admin_bp.route("/api/reports", methods=["GET"])
@role_required_api("ADMIN")
def api_reports():

    reports = AdminController.get_reports()

    return jsonify({"success": True, "reports": reports}), 200
