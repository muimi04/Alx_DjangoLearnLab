from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these columns in list view
    list_filter = ('publication_year', 'author')            # Add filters on the sidebar
    search_fields = ('title', 'author')                     # Enable search bar for title and author

