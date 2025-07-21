from django.contrib import admin
from .models import Book

# Customize the admin display
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show in admin list
    list_filter = ('publication_year', 'author')            # Add sidebar filters
    search_fields = ('title', 'author')                     # Enable search functionality


