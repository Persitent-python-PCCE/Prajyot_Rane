from flask import Blueprint, render_template, request, redirect, url_for, session

from controllers.auth_controller import AuthController

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    user, error = AuthController.register(name, email, password)

    if error:
        return render_template("register.html", error=error)

    return redirect(url_for("auth.login"))


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

    email = request.form.get("email")
    password = request.form.get("password")

    user, error = AuthController.login(email, password)

    if error:
        return render_template("login.html", error=error)

    session["user_id"] = user.id
    session["user_name"] = user.name
    session["role"] = user.role.name

    return redirect(url_for("dashboard"))


@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("auth.login"))
