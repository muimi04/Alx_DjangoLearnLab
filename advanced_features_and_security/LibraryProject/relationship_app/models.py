from django.db import models
from django.conf import settings  # ✅ Use this to support custom user models

# Existing models
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "Can add a new book"),
            ("can_edit_book", "Can edit book"),
            ("can_delete_book", "Can delete book"),
            ("can_change_book", "Can change book"),
        ]

# ✅ UserProfile now supports custom user model
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
