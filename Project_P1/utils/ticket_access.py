from functools import wraps

from flask import session, jsonify

from flask_jwt_extended import get_jwt_identity, get_jwt

from dao.ticket_dao import TicketDAO


def ticket_access_required(view):

    @wraps(view)
    def wrapper(ticket_id, *args, **kwargs):

        ticket = TicketDAO.find_by_id(ticket_id)

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

        return view(ticket_id, *args, **kwargs)

    return wrapper


def ticket_access_required_api(view):

    @wraps(view)
    def wrapper(ticket_id, *args, **kwargs):

        ticket = TicketDAO.find_by_id(ticket_id)

        if not ticket:
            return jsonify({"success": False, "error": "Ticket not found"}), 404

        user_id = int(get_jwt_identity())

        claims = get_jwt()

        role = claims.get("role")

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

        return view(ticket_id, *args, **kwargs)

    return wrapper
