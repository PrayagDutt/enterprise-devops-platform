"""
app/models/task.py — Task Model
=================================
Defines the `tasks` database table and the Task domain object.

Status lifecycle:  todo → in_progress → done
Priority levels:   low | medium | high

The use of db.Enum maps directly to a MySQL ENUM column type, giving us
database-level validation in addition to application-level checks.
"""

import enum
from datetime import datetime, timezone

from app.extensions import db


# ── Enum definitions ──────────────────────────────────────────────────────────
# Using Python enums keeps the allowed values DRY — referenced in both the
# model column definition and in WTForms choices.

class TaskStatus(str, enum.Enum):
    """Lifecycle stages of a task."""
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TaskPriority(str, enum.Enum):
    """Priority level of a task."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


# ── Model ─────────────────────────────────────────────────────────────────────

class Task(db.Model):
    """Represents a single task owned by a User.

    Each task belongs to exactly one user (user_id FK). The `owner`
    back-reference lets us do task.owner.username etc.
    """

    __tablename__ = "tasks"

    # ── Primary key ───────────────────────────────────────────────────────
    id = db.Column(db.Integer, primary_key=True)

    # ── Content fields ────────────────────────────────────────────────────
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)

    # ── Enum columns — stored as VARCHAR in SQLite, ENUM in MySQL ─────────
    status = db.Column(
        db.Enum(TaskStatus),
        nullable=False,
        default=TaskStatus.TODO,
        index=True,  # Frequently filtered on — add an index
    )
    priority = db.Column(
        db.Enum(TaskPriority),
        nullable=False,
        default=TaskPriority.MEDIUM,
        index=True,
    )

    # ── Optional scheduling ───────────────────────────────────────────────
    due_date = db.Column(db.Date, nullable=True)

    # ── Timestamps ────────────────────────────────────────────────────────
    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # ── Foreign key ───────────────────────────────────────────────────────
    # Links this task to the user who created it.
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # ── Relationship ──────────────────────────────────────────────────────
    # `back_populates` keeps both sides of the relationship in sync.
    owner = db.relationship("User", back_populates="tasks")

    # ── Computed properties ───────────────────────────────────────────────

    @property
    def is_overdue(self) -> bool:
        """Return True if the task has a due date that has passed and isn't done."""
        if self.due_date is None or self.status == TaskStatus.DONE:
            return False
        return self.due_date < datetime.now(timezone.utc).date()

    @property
    def status_label(self) -> str:
        """Human-readable status label for display in templates."""
        labels = {
            TaskStatus.TODO: "To Do",
            TaskStatus.IN_PROGRESS: "In Progress",
            TaskStatus.DONE: "Done",
        }
        return labels.get(self.status, self.status.value)

    @property
    def priority_label(self) -> str:
        """Human-readable priority label."""
        return self.priority.value.capitalize()

    def __repr__(self) -> str:
        return f"<Task id={self.id} title={self.title!r} status={self.status.value}>"
