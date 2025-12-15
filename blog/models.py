from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    # -----------------------------
    # Metadata
    # -----------------------------
    class Meta:
        ordering = ["created_on"]  # oldest comments first

    # -----------------------------
    # String representation
    # -----------------------------
    def __str__(self):
        return f"Comment '{self.body}' by {self.author.username}"
