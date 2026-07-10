# app/blueprints/main/__init__.py
# Instantiates the 'main' blueprint.
# Imported by app/__init__.py → _register_blueprints()

from flask import Blueprint

main_bp = Blueprint("main", __name__, template_folder="../../templates")

from app.blueprints.main import routes  # noqa: E402, F401 — side-effect import
