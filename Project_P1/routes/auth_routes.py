from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    jsonify,
)

from flask_jwt_extended import create_access_token

from controllers.auth_controller import AuthController

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    user, error = AuthController.register_user(name, email, password)

    if error:
        return render_template("register.html", error=error)

    return redirect(url_for("auth.login"))


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

    email = request.form.get("email")
    password = request.form.get("password")

    user, error = AuthController.login_user(email, password)

    if error:
        return render_template("login.html", error=error)

    if user.role.name == "ADMIN":
        return redirect(url_for("admin.dashboard"))

    if user.role.name == "SUPPORT_AGENT":
        return redirect(url_for("agent.dashboard"))

    return redirect(url_for("ticket.my_tickets"))


@auth_bp.route("/api/register", methods=["POST"])
def api_register():

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"success": False, "error": "Request body is required"}), 400

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    user, error = AuthController.register_user(name, email, password)

    if error:
        return jsonify({"success": False, "error": error}), 400

    return (
        jsonify(
            {
                "success": True,
                "message": "Registration successful",
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "role": user.role.name,
                },
            }
        ),
        201,
    )


@auth_bp.route("/api/login", methods=["POST"])
def api_login():

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"success": False, "error": "Request body is required"}), 400

    email = data.get("email")
    password = data.get("password")

    user, error = AuthController.login_user(email, password)

    if error:
        return jsonify({"success": False, "error": error}), 401

    access_token = create_access_token(
        identity=str(user.id),
        additional_claims={
            "role": user.role.name,
            "email": user.email,
            "name": user.name,
        },
    )

    return (
        jsonify(
            {
                "success": True,
                "message": "Login successful",
                "access_token": access_token,
                "token_type": "Bearer",
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "role": user.role.name,
                },
            }
        ),
        200,
    )


@auth_bp.route("/logout")
def logout():

    AuthController.logout_user()

    return redirect(url_for("home"))
