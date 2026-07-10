"""
app/models/user.py — User Model
=================================
Defines the `users` database table and the User domain object.

Flask-Login integration:
    UserMixin provides default implementations for is_authenticated,
    is_active, is_anonymous, and get_id() — required by Flask-Login.

Password security:
    Passwords are never stored in plain text. Werkzeug's PBKDF2-SHA256
    hashing is used via generate_password_hash / check_password_hash.
"""

from datetime import datetime, timezone

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app.extensions import db


class User(UserMixin, db.Model):
    """Represents an authenticated user of the task manager.

    Relationships:
        tasks: One-to-many → Task (a user owns many tasks)
    """

    __tablename__ = "users"

    # ── Primary key ───────────────────────────────────────────────────────
    id = db.Column(db.Integer, primary_key=True)

    # ── Identity fields ───────────────────────────────────────────────────
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(254), unique=True, nullable=False, index=True)

    # ── Authentication ────────────────────────────────────────────────────
    # Stores the hashed password — never the raw password.
    password_hash = db.Column(db.String(256), nullable=False)

    # ── Status ────────────────────────────────────────────────────────────
    # Allows soft-disabling an account without deleting it.
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    # ── Timestamps ────────────────────────────────────────────────────────
    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    last_login_at = db.Column(db.DateTime(timezone=True), nullable=True)

    # ── Relationships ─────────────────────────────────────────────────────
    # `cascade="all, delete-orphan"` ensures tasks are deleted when the
    # owning user is deleted, keeping the DB referentially clean.
    tasks = db.relationship(
        "Task",
        back_populates="owner",
        cascade="all, delete-orphan",
        lazy="dynamic",  # Returns a query object; allows chained filters
    )

    # ── Password helpers ──────────────────────────────────────────────────

    def set_password(self, plain_password: str) -> None:
        """Hash and store a new password (never stores plain text)."""
        self.password_hash = generate_password_hash(plain_password)

    def check_password(self, plain_password: str) -> bool:
        """Return True if `plain_password` matches the stored hash."""
        return check_password_hash(self.password_hash, plain_password)

    # ── Flask-Login override ──────────────────────────────────────────────

    def get_id(self) -> str:
        """Return user id as string — required by Flask-Login."""
        return str(self.id)

    # ── Utility ───────────────────────────────────────────────────────────

    @property
    def task_count(self) -> int:
        """Total number of tasks owned by this user."""
        return self.tasks.count()

    def __repr__(self) -> str:
        return f"<User id={self.id} username={self.username!r}>"
