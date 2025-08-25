from django.conf import settings
from django.db import models


class Post(models.Model):
    # who wrote it
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    title = models.CharField(max_length=255)
    content = models.TextField()

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)  # set once
    updated_at = models.DateTimeField(auto_now=True)      # update on save

    class Meta:
        ordering = ['-created_at']  # newest first

    def __str__(self):
        return f"{self.title} (by {self.author.username})"


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']  # oldest first within a post thread

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post_id}"
