from flask import Blueprint, render_template, redirect, url_for, session, request

from controllers.admin_controller import AdminController

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if session.get("role") != "ADMIN":
        return "Unauthorized", 403

    tickets, agents = AdminController.get_dashboard_data()

    return render_template("admin_dashboard.html", tickets=tickets, agents=agents)


@admin_bp.route("/agents/create", methods=["GET", "POST"])
def create_agent():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if session.get("role") != "ADMIN":
        return "Unauthorized", 403

    if request.method == "GET":
        return render_template("create_agent.html")

    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    agent, error = AdminController.create_agent(name, email, password)

    if error:
        return render_template("create_agent.html", error=error)

    return redirect(url_for("admin.dashboard"))
