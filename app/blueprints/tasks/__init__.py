# app/blueprints/tasks/__init__.py
# Instantiates the 'tasks' blueprint.
# Registered in app/__init__.py with url_prefix="/tasks".

from flask import Blueprint

tasks_bp = Blueprint("tasks", __name__, template_folder="../../templates")

from app.blueprints.tasks import routes  # noqa: E402, F401
