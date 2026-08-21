from flask import Blueprint, render_template, request, redirect, url_for, session

from dao.ticket_category_dao import TicketCategoryDAO
from controllers.ticket_controller import TicketController

ticket_bp = Blueprint("ticket", __name__, url_prefix="/tickets")


@ticket_bp.route("/create", methods=["GET", "POST"])
def create_ticket():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

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
def my_tickets():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    tickets = TicketController.get_user_tickets(session["user_id"])

    return render_template("my_tickets.html", tickets=tickets)


@ticket_bp.route("/<int:ticket_id>")
def ticket_details(ticket_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    ticket = TicketController.get_ticket(ticket_id)

    if not ticket:
        return "Ticket not found", 404

    user_id = session["user_id"]
    role = session["role"]

    # Employee can view only their own tickets
    if role == "EMPLOYEE":
        if ticket.requester_id != user_id:
            return "Unauthorized", 403

    # Support agent can view tickets assigned to them
    elif role == "SUPPORT_AGENT":

        assigned = any(
            assignment.agent_id == user_id for assignment in ticket.assignments
        )

        if not assigned:
            return "Unauthorized", 403

    # Admin can view any ticket
    elif role == "ADMIN":
        pass

    else:
        return "Unauthorized", 403

    return render_template("ticket_details.html", ticket=ticket)
