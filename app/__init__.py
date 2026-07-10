"""
app/__init__.py — Application Factory
=======================================
The `create_app()` factory pattern allows the app to be instantiated with
different configurations (e.g., testing vs production) and prevents circular
imports by deferring extension and blueprint registration until called.

Usage:
    from app import create_app
    app = create_app("production")
"""

import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask, jsonify, render_template

from config import config_map
from app.extensions import db, login_manager, migrate, csrf


def create_app(config_name: str | None = None) -> Flask:
    """Create and configure the Flask application instance.

    Args:
        config_name: One of 'development', 'production', 'testing'.
                     Falls back to APP_ENV env var, then 'development'.

    Returns:
        A fully configured Flask application object.
    """
    # ── Resolve which config to use ───────────────────────────────────────
    if config_name is None:
        config_name = os.getenv("APP_ENV", "development")

    app = Flask(__name__, template_folder="templates", static_folder="static")

    # ── Load configuration class ──────────────────────────────────────────
    config_class = config_map.get(config_name, config_map["development"])
    app.config.from_object(config_class)

    # ── Initialise extensions (init_app pattern) ──────────────────────────
    _init_extensions(app)

    # ── Register blueprints ───────────────────────────────────────────────
    _register_blueprints(app)

    # ── Register error handlers ───────────────────────────────────────────
    _register_error_handlers(app)

    # ── Configure logging ─────────────────────────────────────────────────
    _configure_logging(app)

    app.logger.info(f"DevOps Task Manager started in '{config_name}' mode.")
    return app


# ── Private helpers ───────────────────────────────────────────────────────────

def _init_extensions(app: Flask) -> None:
    """Bind all extension singletons to this app instance."""
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # User loader callback — tells Flask-Login how to reload the user object
    # from the user_id stored in the session cookie.
    from app.models.user import User  # local import avoids circular dependency

    @login_manager.user_loader
    def load_user(user_id: str):
        return db.session.get(User, int(user_id))


def _register_blueprints(app: Flask) -> None:
    """Import and register all blueprint modules."""
    from app.blueprints.main import main_bp
    from app.blueprints.auth import auth_bp
    from app.blueprints.tasks import tasks_bp

    app.register_blueprint(main_bp)                      # /
    app.register_blueprint(auth_bp, url_prefix="/auth")  # /auth/...
    app.register_blueprint(tasks_bp, url_prefix="/tasks")  # /tasks/...


def _register_error_handlers(app: Flask) -> None:
    """Register custom error pages for HTTP 404 and 500."""

    @app.errorhandler(404)
    def page_not_found(error):
        app.logger.warning(f"404 Not Found: {error}")
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        # Roll back any partial DB transaction so the session stays clean.
        db.session.rollback()
        app.logger.error(f"500 Internal Server Error: {error}")
        return render_template("errors/500.html"), 500


def _configure_logging(app: Flask) -> None:
    """Set up rotating file logging and optionally stream to stdout.

    In containerised environments, set LOG_TO_STDOUT=true so logs are
    captured by the container runtime (Docker / Kubernetes) without needing
    a persistent volume for log files.
    """
    log_level = getattr(logging, app.config.get("LOG_LEVEL", "INFO"), logging.INFO)

    # Formatter: timestamp | level | module | message
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)-8s %(name)s — %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    if app.config.get("LOG_TO_STDOUT"):
        # Stream handler for container / CI environments
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        app.logger.addHandler(stream_handler)
    else:
        # Rotating file handler — max 5 MB per file, keep last 5 files
        log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
        os.makedirs(log_dir, exist_ok=True)
        file_handler = RotatingFileHandler(
            os.path.join(log_dir, "devops_taskmanager.log"),
            maxBytes=5 * 1024 * 1024,  # 5 MB
            backupCount=5,
        )
        file_handler.setFormatter(formatter)
        app.logger.addHandler(file_handler)

    app.logger.setLevel(log_level)
    # Suppress verbose SQLAlchemy logs in non-debug modes
    if not app.debug:
        logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
