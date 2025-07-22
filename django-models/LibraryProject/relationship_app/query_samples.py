import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books_by_author = author.books.all()
print("Books by", author.name)
for book in books_by_author:
    print("-", book.title)

# Query 2: List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("\nBooks in", library.name)
for book in books_in_library:
    print("-", book.title)

# Query 3: Retrieve the librarian for a library
librarian = library.librarian
print(f"\nLibrarian of {library.name} is {librarian.name}")
