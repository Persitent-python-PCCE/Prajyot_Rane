from functools import wraps

from flask import session, redirect, url_for, jsonify

from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt


def login_required(view):

    @wraps(view)
    def wrapper(*args, **kwargs):

        if "user_id" not in session:
            return redirect(url_for("auth.login"))

        return view(*args, **kwargs)

    return wrapper


def role_required(*roles):

    def decorator(view):

        @wraps(view)
        def wrapper(*args, **kwargs):

            if "user_id" not in session:
                return redirect(url_for("auth.login"))

            if session.get("role") not in roles:
                return "Unauthorized", 403

            return view(*args, **kwargs)

        return wrapper

    return decorator


def login_required_api(view):

    @wraps(view)
    @jwt_required()
    def wrapper(*args, **kwargs):
        return view(*args, **kwargs)

    return wrapper


def role_required_api(*roles):

    def decorator(view):

        @wraps(view)
        @jwt_required()
        def wrapper(*args, **kwargs):

            claims = get_jwt()

            if claims.get("role") not in roles:
                return jsonify({"success": False, "error": "Unauthorized"}), 403

            return view(*args, **kwargs)

        return wrapper

    return decorator


def get_api_user_id():

    return int(get_jwt_identity())
