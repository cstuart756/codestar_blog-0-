// Comments editing and deletion

const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
const commentText = document.getElementById("id_body");

const editButtons = document.getElementsByClassName("btn-edit");

// Delete modal elements (Bootstrap 5)
const deleteModalEl = document.getElementById("deleteModal");
const deleteConfirm = document.getElementById("deleteConfirm");
const deleteButtons = document.getElementsByClassName("btn-delete");

const deleteModal = deleteModalEl ? new bootstrap.Modal(deleteModalEl) : null;

// Determine slug from URL: /<slug>/...
// If your URL has a prefix like /blog/<slug>/, then adjust this logic.
const pathParts = window.location.pathname.split("/").filter(Boolean);
const postSlug = pathParts[0];

// EDIT: populate textarea and set form action to /<slug>/edit_comment/<id>
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        const commentId = e.target.getAttribute("comment_id");
        const commentBodyEl = document.getElementById(`comment${commentId}`);

        if (!commentId || !commentBodyEl || !commentForm || !commentText || !submitButton) {
            return;
        }

        commentText.value = commentBodyEl.innerText.trim();
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `/${postSlug}/edit_comment/${commentId}`);
    });
}

// DELETE: open modal and set confirm link to /<slug>/delete_comment/<id>
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        const commentId = e.target.getAttribute("comment_id");

        if (!commentId || !deleteConfirm || !deleteModal) {
            return;
        }

        deleteConfirm.href = `/${postSlug}/delete_comment/${commentId}`;
        deleteModal.show();
    });
}
