from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Extends Django's built-in user with social fields.
    - bio: text about the user
    - profile_picture: stored as an uploaded image
    - followers: users who follow *this* user
      symmetrical=False so A following B does not imply B follows A
      related_name='following' allows reverse lookup: user.following.all()
    """
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField(
        'self', blank=True, symmetrical=False, related_name='following'
    )

    def __str__(self) -> str:
        return self.username

    # Convenience helpers
    def follow(self, other: 'CustomUser'):
        if other != self:
            other.followers.add(self)

    def unfollow(self, other: 'CustomUser'):
        if other != self:
            other.followers.remove(self)

    def is_following(self, other: 'CustomUser') -> bool:
        """Check if this user is following another user."""
        return other in self.following.all()

    def get_following(self):
        """Return a queryset of all users this user follows."""
        return self.following.all()

    def get_feed_posts(self):
        """Return posts from users this user follows, newest first."""
        from posts.models import Post  # import here to avoid circular import
        return Post.objects.filter(author__in=self.get_following()).order_by('-created_at')
