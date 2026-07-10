# app/blueprints/auth/__init__.py
# Instantiates the 'auth' blueprint.
# Registered in app/__init__.py with url_prefix="/auth".

from flask import Blueprint

auth_bp = Blueprint("auth", __name__, template_folder="../../templates")

from app.blueprints.auth import routes  # noqa: E402, F401
