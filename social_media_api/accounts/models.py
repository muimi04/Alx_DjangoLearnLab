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

    # Convenience helpers (optional; nice for future endpoints)
    def follow(self, other: 'CustomUser'):
        if other != self:
            other.followers.add(self)

    def unfollow(self, other: 'CustomUser'):
        if other != self:
            other.followers.remove(self)
