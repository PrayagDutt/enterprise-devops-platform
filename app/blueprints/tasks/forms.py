"""
app/blueprints/tasks/forms.py — Task Forms
==========================================
WTForms form for creating and editing tasks.

Uses SelectField with enum-based choices so the UI options always stay
in sync with the TaskStatus and TaskPriority enum definitions in the model.
"""

from datetime import date

from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional

from app.models.task import TaskPriority, TaskStatus


class TaskForm(FlaskForm):
    """Shared form used for both creating and editing tasks.

    The `obj` parameter passed to form instantiation (in edit routes) will
    pre-populate fields with the current task's values automatically.
    """

    title = StringField(
        "Task Title",
        validators=[
            DataRequired(message="Title is required."),
            Length(max=200, message="Title cannot exceed 200 characters."),
        ],
        render_kw={"placeholder": "What needs to be done?", "autofocus": True},
    )

    description = TextAreaField(
        "Description",
        validators=[Optional()],
        render_kw={
            "placeholder": "Add more details about this task (optional)…",
            "rows": 4,
        },
    )

    # Build choices from the enum so they stay in sync with the model
    status = SelectField(
        "Status",
        choices=[
            (TaskStatus.TODO.value, "To Do"),
            (TaskStatus.IN_PROGRESS.value, "In Progress"),
            (TaskStatus.DONE.value, "Done"),
        ],
        default=TaskStatus.TODO.value,
        validators=[DataRequired()],
    )

    priority = SelectField(
        "Priority",
        choices=[
            (TaskPriority.LOW.value, "🟢 Low"),
            (TaskPriority.MEDIUM.value, "🟡 Medium"),
            (TaskPriority.HIGH.value, "🔴 High"),
        ],
        default=TaskPriority.MEDIUM.value,
        validators=[DataRequired()],
    )

    due_date = DateField(
        "Due Date",
        validators=[Optional()],
        render_kw={"min": date.today().isoformat()},
    )

    submit = SubmitField("Save Task")
