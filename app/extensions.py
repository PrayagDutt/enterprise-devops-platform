"""
app/extensions.py — Flask Extension Singletons
================================================
All Flask extensions are instantiated here WITHOUT being bound to an app.
They are registered with the app inside create_app() using the init_app()
pattern, which prevents circular imports and supports the application factory.

Import these objects wherever you need them:
    from app.extensions import db, login_manager, migrate
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

# ── SQLAlchemy ORM ────────────────────────────────────────────────────────────
# Provides the `db` object used in all models for table definitions and queries.
db = SQLAlchemy()

# ── Flask-Login ───────────────────────────────────────────────────────────────
# Manages user session lifecycle (login, logout, remember-me, @login_required).
login_manager = LoginManager()

# The view function name that unauthenticated users are redirected to.
login_manager.login_view = "auth.login"
# Flash message category used for the "please log in" message.
login_manager.login_message_category = "warning"
login_manager.login_message = "Please log in to access this page."

# ── Flask-Migrate (Alembic) ───────────────────────────────────────────────────
# Handles schema migrations via `flask db init / migrate / upgrade` CLI commands.
migrate = Migrate()

# ── Flask-WTF CSRF Protection ─────────────────────────────────────────────────
# Automatically adds CSRF protection to all WTForms-based forms.
csrf = CSRFProtect()
