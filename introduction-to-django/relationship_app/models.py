# relationship_app/models.py

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Library(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, related_name='books', on_delete=models.CASCADE)
    publication_year = models.IntegerField()
