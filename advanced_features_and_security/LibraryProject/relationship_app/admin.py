from django.contrib import admin
from .models import Author, Book, Library, UserProfile  # ✅ FIXED import

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(UserProfile)
