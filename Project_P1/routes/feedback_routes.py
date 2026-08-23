from flask import Blueprint, request, session, jsonify, redirect, url_for

from flask_jwt_extended import get_jwt

from utils.auth_decorators import login_required, login_required_api, get_api_user_id

from utils.ticket_access import ticket_access_required, ticket_access_required_api

from controllers.feedback_controller import FeedbackController
from dao.feedback_dao import FeedbackDAO

feedback_bp = Blueprint("feedback", __name__, url_prefix="/feedback")


@feedback_bp.route("/tickets/<int:ticket_id>", methods=["POST"])
@login_required
@ticket_access_required
def create_feedback(ticket_id):

    rating = request.form.get("rating")
    comment = request.form.get("comment")

    feedback, error = FeedbackController.create_feedback(
        ticket_id=ticket_id, user_id=session["user_id"], rating=rating, comment=comment
    )

    if error:
        return error, 400

    return redirect(url_for("ticket.ticket_details", ticket_id=ticket_id))


@feedback_bp.route("/api/tickets/<int:ticket_id>", methods=["POST"])
@login_required_api
@ticket_access_required_api
def api_create_feedback(ticket_id):

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"success": False, "error": "Request body is required"}), 400

    rating = data.get("rating")
    comment = data.get("comment")

    feedback, error = FeedbackController.create_feedback(
        ticket_id=ticket_id, user_id=get_api_user_id(), rating=rating, comment=comment
    )

    if error:
        return jsonify({"success": False, "error": error}), 400

    return (
        jsonify(
            {
                "success": True,
                "message": "Feedback submitted successfully",
                "feedback": {
                    "id": feedback.id,
                    "ticket_id": feedback.ticket_id,
                    "user_id": feedback.user_id,
                    "rating": feedback.rating,
                    "comment": feedback.comment,
                    "created_at": (
                        feedback.created_at.isoformat() if feedback.created_at else None
                    ),
                },
            }
        ),
        201,
    )


@feedback_bp.route("/api/tickets/<int:ticket_id>", methods=["GET"])
@login_required_api
@ticket_access_required_api
def api_get_feedback(ticket_id):

    feedback = FeedbackDAO.find_by_ticket(ticket_id)

    if not feedback:
        return jsonify({"success": True, "feedback": None}), 200

    return (
        jsonify(
            {
                "success": True,
                "feedback": {
                    "id": feedback.id,
                    "ticket_id": feedback.ticket_id,
                    "user_id": feedback.user_id,
                    "rating": feedback.rating,
                    "comment": feedback.comment,
                    "created_at": (
                        feedback.created_at.isoformat() if feedback.created_at else None
                    ),
                },
            }
        ),
        200,
    )
