"""
app/blueprints/main/routes.py — Main Blueprint
================================================
Handles the root dashboard route and the /health endpoint.

/health is designed for:
  - Docker HEALTHCHECK
  - Kubernetes liveness / readiness probes
  - Load balancer health checks
  - Uptime monitoring tools (UptimeRobot, Pingdom, etc.)
"""

from datetime import datetime, timezone

from flask import current_app, jsonify, render_template
from flask_login import current_user, login_required
from sqlalchemy import text

from app.extensions import db
from app.models.task import Task, TaskStatus
from . import main_bp


@main_bp.route("/")
@login_required
def dashboard():
    """Main dashboard — shows task summary statistics for the logged-in user."""
    user_tasks = current_user.tasks  # Lazy dynamic query object

    # Count tasks grouped by status for the summary cards
    total = user_tasks.count()
    todo_count = user_tasks.filter_by(status=TaskStatus.TODO).count()
    in_progress_count = user_tasks.filter_by(status=TaskStatus.IN_PROGRESS).count()
    done_count = user_tasks.filter_by(status=TaskStatus.DONE).count()

    # Fetch the 5 most recently updated tasks for the activity feed
    recent_tasks = (
        user_tasks.order_by(Task.updated_at.desc()).limit(5).all()
    )

    # Overdue tasks — due_date < today AND not done
    today = datetime.now(timezone.utc).date()
    overdue_tasks = [
        t for t in user_tasks.all()
        if t.due_date and t.due_date < today and t.status != TaskStatus.DONE
    ]

    current_app.logger.debug(
        f"Dashboard loaded for user={current_user.username}: "
        f"total={total}, overdue={len(overdue_tasks)}"
    )

    return render_template(
        "main/dashboard.html",
        total=total,
        todo_count=todo_count,
        in_progress_count=in_progress_count,
        done_count=done_count,
        recent_tasks=recent_tasks,
        overdue_tasks=overdue_tasks,
    )


@main_bp.route("/health")
def health():
    """Health check endpoint — returns JSON status including DB connectivity.

    HTTP 200 → healthy
    HTTP 503 → unhealthy (DB unreachable)

    Example response:
        {
            "status": "ok",
            "database": "ok",
            "timestamp": "2025-01-01T00:00:00Z",
            "version": "1.0.0"
        }
    """
    health_data = {
        "status": "ok",
        "database": "unknown",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "app": "DevOps Task Manager",
        "version": "1.0.0",
    }
    http_status = 200

    try:
        # Execute a lightweight query to verify DB connectivity.
        # `text()` is required for raw SQL in SQLAlchemy 2.x.
        db.session.execute(text("SELECT 1"))
        health_data["database"] = "ok"
        current_app.logger.debug("Health check: DB OK")
    except Exception as exc:
        # If the DB is unreachable, report degraded status but don't crash.
        health_data["status"] = "degraded"
        health_data["database"] = "unreachable"
        http_status = 503
        current_app.logger.error(f"Health check DB error: {exc}")

    return jsonify(health_data), http_status
