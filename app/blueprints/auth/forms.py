"""
app/blueprints/auth/forms.py — Authentication Forms
=====================================================
WTForms-based form classes for login and registration.
Flask-WTF automatically adds CSRF token validation to all forms.

Validators ensure data integrity before any DB interaction occurs,
providing a clean separation between input validation and business logic.
"""

from flask_wtf import FlaskForm
from wtforms import BooleanField, EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    Regexp,
    ValidationError,
)

from app.models.user import User


class LoginForm(FlaskForm):
    """Form for existing users to authenticate."""

    # Accept login with either username or email (handled in route)
    username = StringField(
        "Username",
        validators=[
            DataRequired(message="Username is required."),
            Length(max=80),
        ],
        render_kw={"placeholder": "Enter your username", "autofocus": True},
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(message="Password is required.")],
        render_kw={"placeholder": "Enter your password"},
    )
    remember_me = BooleanField("Keep me signed in")
    submit = SubmitField("Sign In")


class RegisterForm(FlaskForm):
    """Form for new user registration with uniqueness validation."""

    username = StringField(
        "Username",
        validators=[
            DataRequired(message="Username is required."),
            Length(min=3, max=80, message="Username must be 3–80 characters."),
            # Only allow alphanumeric + underscore — prevents injection attempts
            Regexp(
                r"^[\w]+$",
                message="Username may only contain letters, numbers, and underscores.",
            ),
        ],
        render_kw={"placeholder": "Choose a username", "autofocus": True},
    )
    email = EmailField(
        "Email Address",
        validators=[
            DataRequired(message="Email is required."),
            Email(message="Please enter a valid email address."),
            Length(max=254),
        ],
        render_kw={"placeholder": "you@example.com"},
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Password is required."),
            Length(min=8, message="Password must be at least 8 characters."),
        ],
        render_kw={"placeholder": "Min. 8 characters"},
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(message="Please confirm your password."),
            EqualTo("password", message="Passwords must match."),
        ],
        render_kw={"placeholder": "Repeat your password"},
    )
    submit = SubmitField("Create Account")

    # ── Cross-field / DB-level validators ────────────────────────────────
    # WTForms calls validate_<fieldname>() automatically during form.validate().

    def validate_username(self, field):
        """Reject registration if the username is already taken."""
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("That username is already taken. Please choose another.")

    def validate_email(self, field):
        """Reject registration if the email address is already registered."""
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError("An account with that email already exists.")
