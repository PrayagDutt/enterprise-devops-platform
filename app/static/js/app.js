/**
 * app.js — DevOps Task Manager Client-Side Logic
 * ================================================
 * Vanilla JS — no external runtime dependencies.
 *
 * Sections:
 *   1. Sidebar toggle (mobile)
 *   2. Auto-dismiss flash messages
 *   3. Delete confirmation modal
 *   4. Password visibility toggle
 *   5. Sort/filter form auto-submit on select change
 *   6. Confirm before leaving unsaved forms
 */

'use strict';

/* ── 1. Sidebar Toggle (mobile) ─────────────────────────────────────────── */

/**
 * Opens/closes the sidebar on mobile viewports.
 * Called via the hamburger button onclick in base.html.
 */
function toggleSidebar() {
  const sidebar  = document.getElementById('sidebar');
  const backdrop = document.getElementById('sidebarBackdrop');
  if (!sidebar) return;

  const isOpen = sidebar.classList.toggle('open');
  if (backdrop) backdrop.classList.toggle('show', isOpen);
  // Prevent body scroll when sidebar is open on mobile
  document.body.style.overflow = isOpen ? 'hidden' : '';
}

/* Close sidebar when pressing Escape */
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    const sidebar = document.getElementById('sidebar');
    if (sidebar && sidebar.classList.contains('open')) {
      toggleSidebar();
    }
  }
});

/* ── 2. Auto-dismiss Flash Messages ────────────────────────────────────── */

/**
 * Flash messages auto-dismiss after 5 seconds.
 * Uses the Bootstrap dismiss API so the slide-out animation plays.
 */
document.addEventListener('DOMContentLoaded', () => {
  const flashAlerts = document.querySelectorAll('.flash-alert');

  flashAlerts.forEach((alertEl) => {
    // Give 'success' and 'info' messages a 4s timeout; warnings/errors stay longer
    const isUrgent = alertEl.classList.contains('alert-danger') ||
                     alertEl.classList.contains('alert-warning');
    const timeout = isUrgent ? 8000 : 4500;

    setTimeout(() => {
      // Use Bootstrap's dismiss so the fade-out animation runs
      const bsAlert = bootstrap.Alert.getOrCreateInstance(alertEl);
      if (bsAlert) bsAlert.close();
    }, timeout);
  });
});

/* ── 3. Delete Confirmation Modal ───────────────────────────────────────── */

/**
 * Populates and shows the delete confirmation modal.
 * Called via onclick on each delete button in the task table / edit page.
 *
 * @param {number} taskId   - The task's database ID
 * @param {string} taskName - The task title to display in the modal body
 */
function confirmDelete(taskId, taskName) {
  const modal        = document.getElementById('deleteModal');
  const nameEl       = document.getElementById('delete-task-name');
  const deleteForm   = document.getElementById('delete-form');

  if (!modal || !nameEl || !deleteForm) return;

  // Update modal content with the specific task details
  nameEl.textContent = taskName;

  // Build the POST URL dynamically: /tasks/<id>/delete
  deleteForm.action = `/tasks/${taskId}/delete`;

  // Show the Bootstrap modal
  const bsModal = bootstrap.Modal.getOrCreateInstance(modal);
  bsModal.show();
}

/* ── 4. Password Visibility Toggle ─────────────────────────────────────── */

/**
 * Toggles an <input type="password"> between text and password visibility.
 * Called via onclick on the eye-icon button.
 *
 * @param {string} inputId - ID of the password input element
 * @param {string} iconId  - ID of the Bootstrap icon element
 */
function togglePasswordVisibility(inputId, iconId) {
  const input = document.getElementById(inputId);
  const icon  = document.getElementById(iconId);
  if (!input || !icon) return;

  const isHidden = input.type === 'password';
  input.type = isHidden ? 'text' : 'password';

  // Swap the icon between eye and eye-slash
  icon.className = isHidden ? 'bi bi-eye-slash' : 'bi bi-eye';
}

/* ── 5. Filter Form — auto-submit on select change ──────────────────────── */

/**
 * Automatically submits the filter form when a <select> value changes,
 * providing an instant filter UX without needing an explicit "Apply" click.
 * Applies only to the task list page filter form.
 */
document.addEventListener('DOMContentLoaded', () => {
  // These selects trigger an instant form submit on change
  const autoSubmitSelects = ['#select-status', '#select-priority', '#select-sort', '#select-order'];

  autoSubmitSelects.forEach((selector) => {
    const el = document.querySelector(selector);
    if (el) {
      el.addEventListener('change', () => {
        const form = el.closest('form');
        if (form) form.submit();
      });
    }
  });
});

/* ── 6. Unsaved Changes Warning ─────────────────────────────────────────── */

/**
 * Warns the user before navigating away from a form that has unsaved changes.
 * Tracks whether any form field has been modified since the page load.
 */
document.addEventListener('DOMContentLoaded', () => {
  // Only apply to the task create/edit forms
  const trackedForms = ['#create-task-form', '#edit-task-form'];

  trackedForms.forEach((selector) => {
    const form = document.querySelector(selector);
    if (!form) return;

    let isDirty = false;

    // Mark form as dirty on any input change
    form.addEventListener('input', () => { isDirty = true; });
    form.addEventListener('change', () => { isDirty = true; });

    // Reset dirty flag when the form is intentionally submitted
    form.addEventListener('submit', () => { isDirty = false; });

    // Show browser confirm dialog on navigation away
    window.addEventListener('beforeunload', (e) => {
      if (isDirty) {
        e.preventDefault();
        // Modern browsers show a generic message; the custom text is ignored
        e.returnValue = 'You have unsaved changes. Are you sure you want to leave?';
      }
    });
  });
});

/* ── 7. Tooltip Initialisation ──────────────────────────────────────────── */

/**
 * Bootstrap 5 tooltips must be initialised via JS.
 * Selects all elements with data-bs-toggle="tooltip".
 */
document.addEventListener('DOMContentLoaded', () => {
  const tooltipEls = document.querySelectorAll('[data-bs-toggle="tooltip"]');
  tooltipEls.forEach((el) => {
    new bootstrap.Tooltip(el, { trigger: 'hover' });
  });
});
