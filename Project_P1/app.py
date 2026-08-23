from flask import Flask, session, redirect, render_template, jsonify, request
from routes.attachment_routes import attachment_bp
from flask_jwt_extended import JWTManager

from routes.auth_routes import auth_bp
from routes.ticket_routes import ticket_bp
from routes.comment_routes import comment_bp
from routes.agent_routes import agent_bp
from routes.feedback_routes import feedback_bp
from routes.admin_routes import admin_bp

from config import Config
from extensions import db, migrate

from models import (
    Role,
    User,
    TicketCategory,
    Ticket,
    TicketComment,
    TicketAttachment,
    TicketAssignment,
    TicketHistory,
    SlaRule,
    Feedback,
)

jwt = JWTManager()


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)

    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(ticket_bp)
    app.register_blueprint(comment_bp)
    app.register_blueprint(agent_bp)
    app.register_blueprint(feedback_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(attachment_bp)

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/dashboard")
    def dashboard():

        if "user_id" not in session:
            return redirect("/auth/login")

        return f"""
        <h1>Welcome {session["user_name"]}</h1>
        <p>Role: {session["role"]}</p>
        <a href="/auth/logout">Logout</a>
        """

    @app.errorhandler(400)
    def bad_request(error):

        if "/api/" in request.path:
            return jsonify({"success": False, "error": "Bad request"}), 400

        return "Bad Request", 400

    @app.errorhandler(401)
    def unauthorized(error):

        if "/api/" in request.path:
            return jsonify({"success": False, "error": "Authentication required"}), 401

        return "Authentication required", 401

    @app.errorhandler(403)
    def forbidden(error):

        if "/api/" in request.path:
            return jsonify({"success": False, "error": "Unauthorized"}), 403

        return "Unauthorized", 403

    @app.errorhandler(404)
    def not_found(error):

        if "/api/" in request.path:
            return jsonify({"success": False, "error": "Resource not found"}), 404

        return "Page not found", 404

    @app.errorhandler(500)
    def internal_server_error(error):

        db.session.rollback()

        if "/api/" in request.path:
            return jsonify({"success": False, "error": "Internal server error"}), 500

        return "Internal server error", 500

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
