"""
app/blueprints/auth/routes.py — Authentication Routes
======================================================
Handles user registration, login, and logout.

Security practices applied:
  - Passwords never logged or stored in plain text
  - Generic error messages on login failure (don't reveal if username exists)
  - `next` parameter validated to prevent open-redirect attacks
  - `remember_me` sets a persistent session cookie (duration = LoginManager default)
"""

from urllib.parse import urlparse

from flask import current_app, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from app.extensions import db
from app.models.user import User
from . import auth_bp
from .forms import LoginForm, RegisterForm


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """Display login form (GET) and authenticate the user (POST).

    After successful login, redirects to the `next` URL if present and safe,
    otherwise falls back to the dashboard.
    """
    # Redirect already-authenticated users away from the login page
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    form = LoginForm()

    if form.validate_on_submit():
        # Look up the user by username (case-insensitive)
        user = User.query.filter(
            User.username.ilike(form.username.data.strip())
        ).first()

        # Validate credentials — use a generic message to avoid user enumeration
        if user is None or not user.check_password(form.password.data):
            current_app.logger.warning(
                f"Failed login attempt for username='{form.username.data}' "
                f"from IP={request.remote_addr}"
            )
            flash("Invalid username or password. Please try again.", "danger")
            return render_template("auth/login.html", form=form)

        if not user.is_active:
            flash("Your account has been deactivated. Please contact an administrator.", "warning")
            return render_template("auth/login.html", form=form)

        # Persist the login session
        login_user(user, remember=form.remember_me.data)

        # Update last_login_at timestamp
        from datetime import datetime, timezone
        user.last_login_at = datetime.now(timezone.utc)
        db.session.commit()

        current_app.logger.info(f"User '{user.username}' logged in from {request.remote_addr}")
        flash(f"Welcome back, {user.username}! 👋", "success")

        # Safe redirect: only redirect to `next` if it is a relative URL on the same host.
        # This prevents open-redirect attacks (e.g., ?next=http://evil.com).
        next_page = request.args.get("next")
        if next_page:
            parsed = urlparse(next_page)
            if parsed.scheme or parsed.netloc:
                # Absolute URL with scheme/netloc — potential open redirect; ignore it
                next_page = None

        return redirect(next_page or url_for("main.dashboard"))

    return render_template("auth/login.html", form=form, title="Sign In")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """Display registration form (GET) and create a new user account (POST)."""
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    form = RegisterForm()

    if form.validate_on_submit():
        # Create the new user — password is hashed inside set_password()
        new_user = User(
            username=form.username.data.strip(),
            email=form.email.data.lower().strip(),
        )
        new_user.set_password(form.password.data)

        try:
            db.session.add(new_user)
            db.session.commit()
            current_app.logger.info(f"New user registered: '{new_user.username}'")
            flash("Account created successfully! Please sign in.", "success")
            return redirect(url_for("auth.login"))
        except Exception as exc:
            db.session.rollback()
            current_app.logger.error(f"Error creating user: {exc}")
            flash("An error occurred while creating your account. Please try again.", "danger")

    return render_template("auth/register.html", form=form, title="Create Account")


@auth_bp.route("/logout")
@login_required
def logout():
    """Log the current user out and clear their session."""
    username = current_user.username
    logout_user()
    current_app.logger.info(f"User '{username}' logged out.")
    flash("You have been signed out successfully.", "info")
    return redirect(url_for("auth.login"))
