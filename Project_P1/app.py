from flask import Flask, session, redirect, render_template

from routes.comment_routes import comment_bp
from routes.ticket_routes import ticket_bp
from routes.agent_routes import agent_bp
from routes.auth_routes import auth_bp
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


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(ticket_bp)
    app.register_blueprint(comment_bp)
    app.register_blueprint(agent_bp)
    app.register_blueprint(admin_bp)

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/dashboard")
    def dashboard():

        if "user_id" not in session:
            return redirect(url_for("auth.login"))

        return render_template(
            "dashboard.html", user_name=session["user_name"], role=session["role"]
        )

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
