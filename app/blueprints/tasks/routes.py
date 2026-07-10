"""
app/blueprints/tasks/routes.py — Task CRUD Routes
==================================================
Full create / read / update / delete operations for tasks.

All routes require login (@login_required).
Task ownership is enforced on every route — users can only
access their own tasks (404 returned if task not found or not owned).

Route map:
  GET  /tasks/           → list (with search + status filter)
  GET  /tasks/create     → create form
  POST /tasks/create     → save new task
  GET  /tasks/<id>/edit  → edit form (pre-populated)
  POST /tasks/<id>/edit  → save updated task
  POST /tasks/<id>/delete → delete task
  POST /tasks/<id>/toggle → quick-cycle status (todo→in_progress→done→todo)
"""

from flask import abort, current_app, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from app.extensions import db
from app.models.task import Task, TaskPriority, TaskStatus
from . import tasks_bp
from .forms import TaskForm


# ── Helper ────────────────────────────────────────────────────────────────────

def _get_owned_task_or_404(task_id: int) -> Task:
    """Fetch a task by ID that belongs to the current user, or raise 404."""
    task = db.session.get(Task, task_id)
    if task is None or task.user_id != current_user.id:
        abort(404)
    return task


# ── List ──────────────────────────────────────────────────────────────────────

@tasks_bp.route("/")
@login_required
def index():
    """Display paginated, filterable list of the current user's tasks."""
    # --- Query parameters ---
    search_query = request.args.get("q", "").strip()
    status_filter = request.args.get("status", "")
    priority_filter = request.args.get("priority", "")
    sort_by = request.args.get("sort", "updated_at")
    order = request.args.get("order", "desc")
    page = request.args.get("page", 1, type=int)
    per_page = 10  # Items per page

    # --- Base query: only the logged-in user's tasks ---
    query = current_user.tasks

    # --- Apply filters ---
    if search_query:
        # Case-insensitive title/description search using SQL LIKE
        like_pattern = f"%{search_query}%"
        query = query.filter(
            db.or_(
                Task.title.ilike(like_pattern),
                Task.description.ilike(like_pattern),
            )
        )

    if status_filter and status_filter in [s.value for s in TaskStatus]:
        query = query.filter_by(status=TaskStatus(status_filter))

    if priority_filter and priority_filter in [p.value for p in TaskPriority]:
        query = query.filter_by(priority=TaskPriority(priority_filter))

    # --- Apply sorting ---
    sort_column_map = {
        "title": Task.title,
        "status": Task.status,
        "priority": Task.priority,
        "due_date": Task.due_date,
        "created_at": Task.created_at,
        "updated_at": Task.updated_at,
    }
    sort_col = sort_column_map.get(sort_by, Task.updated_at)
    query = query.order_by(sort_col.desc() if order == "desc" else sort_col.asc())

    # --- Paginate ---
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    tasks = pagination.items

    current_app.logger.debug(
        f"Tasks list: user={current_user.username}, "
        f"filter={status_filter}, q={search_query!r}, page={page}"
    )

    return render_template(
        "tasks/index.html",
        tasks=tasks,
        pagination=pagination,
        search_query=search_query,
        status_filter=status_filter,
        priority_filter=priority_filter,
        sort_by=sort_by,
        order=order,
        statuses=TaskStatus,
        priorities=TaskPriority,
        title="My Tasks",
    )


# ── Create ────────────────────────────────────────────────────────────────────

@tasks_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    """Render the new-task form and handle submission."""
    form = TaskForm()

    if form.validate_on_submit():
        task = Task(
            title=form.title.data.strip(),
            description=form.description.data.strip() if form.description.data else None,
            status=TaskStatus(form.status.data),
            priority=TaskPriority(form.priority.data),
            due_date=form.due_date.data,
            user_id=current_user.id,
        )
        try:
            db.session.add(task)
            db.session.commit()
            current_app.logger.info(
                f"Task created: id={task.id} title={task.title!r} "
                f"by user={current_user.username}"
            )
            flash(f"Task '{task.title}' created successfully! ✅", "success")
            return redirect(url_for("tasks.index"))
        except Exception as exc:
            db.session.rollback()
            current_app.logger.error(f"Error creating task: {exc}")
            flash("Failed to create task. Please try again.", "danger")

    return render_template("tasks/create.html", form=form, title="New Task")


# ── Edit ──────────────────────────────────────────────────────────────────────

@tasks_bp.route("/<int:task_id>/edit", methods=["GET", "POST"])
@login_required
def edit(task_id: int):
    """Render the edit form pre-populated with the task's current values."""
    task = _get_owned_task_or_404(task_id)

    # `obj=task` pre-fills form fields from the task's attributes on GET
    form = TaskForm(obj=task)

    # On GET, convert enum objects to their .value strings for SelectFields
    if request.method == "GET":
        form.status.data = task.status.value
        form.priority.data = task.priority.value

    if form.validate_on_submit():
        task.title = form.title.data.strip()
        task.description = form.description.data.strip() if form.description.data else None
        task.status = TaskStatus(form.status.data)
        task.priority = TaskPriority(form.priority.data)
        task.due_date = form.due_date.data

        try:
            db.session.commit()
            current_app.logger.info(
                f"Task updated: id={task.id} title={task.title!r} "
                f"by user={current_user.username}"
            )
            flash(f"Task '{task.title}' updated successfully! ✏️", "success")
            return redirect(url_for("tasks.index"))
        except Exception as exc:
            db.session.rollback()
            current_app.logger.error(f"Error updating task id={task_id}: {exc}")
            flash("Failed to update task. Please try again.", "danger")

    return render_template("tasks/edit.html", form=form, task=task, title="Edit Task")


# ── Delete ────────────────────────────────────────────────────────────────────

@tasks_bp.route("/<int:task_id>/delete", methods=["POST"])
@login_required
def delete(task_id: int):
    """Delete a task (POST only — form submits here from the delete modal)."""
    task = _get_owned_task_or_404(task_id)
    task_title = task.title

    try:
        db.session.delete(task)
        db.session.commit()
        current_app.logger.info(
            f"Task deleted: id={task_id} title={task_title!r} "
            f"by user={current_user.username}"
        )
        flash(f"Task '{task_title}' deleted. 🗑️", "info")
    except Exception as exc:
        db.session.rollback()
        current_app.logger.error(f"Error deleting task id={task_id}: {exc}")
        flash("Failed to delete task. Please try again.", "danger")

    return redirect(url_for("tasks.index"))


# ── Quick Status Toggle ───────────────────────────────────────────────────────

@tasks_bp.route("/<int:task_id>/toggle", methods=["POST"])
@login_required
def toggle(task_id: int):
    """Cycle task status: todo → in_progress → done → todo.

    Allows single-click status updates from the task list without opening
    the full edit form.
    """
    task = _get_owned_task_or_404(task_id)

    # Status cycle order
    cycle = [TaskStatus.TODO, TaskStatus.IN_PROGRESS, TaskStatus.DONE]
    current_index = cycle.index(task.status)
    next_status = cycle[(current_index + 1) % len(cycle)]

    task.status = next_status

    try:
        db.session.commit()
        current_app.logger.info(
            f"Task id={task_id} status toggled to '{next_status.value}' "
            f"by user={current_user.username}"
        )
        flash(f"'{task.title}' marked as {task.status_label}.", "success")
    except Exception as exc:
        db.session.rollback()
        current_app.logger.error(f"Error toggling task id={task_id}: {exc}")
        flash("Failed to update task status.", "danger")

    # Return to the page the user came from (or task list as fallback)
    return redirect(request.referrer or url_for("tasks.index"))
