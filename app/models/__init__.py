# app/models/__init__.py
# Re-export models so Alembic autogenerate can discover all tables
# when running `flask db migrate`.
from app.models.user import User
from app.models.task import Task, TaskStatus, TaskPriority

__all__ = ["User", "Task", "TaskStatus", "TaskPriority"]
