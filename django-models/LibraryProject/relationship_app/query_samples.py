import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
author_name = "J.K. Rowling"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author_name}: {[book.title for book in books_by_author]}")
except Author.DoesNotExist:
    print(f"No author found with name {author_name}")

# Query 2: All books in a specific library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library_name}: {[book.title for book in books_in_library]}")
except Library.DoesNotExist:
    print(f"No library found with name {library_name}")

# Query 3: Retrieve the librarian for a library
# Query 3: Retrieve the librarian for a library
try:
    library = Library.objects.get(name="Downtown Library")
    librarian = library.librarian
    print(f"Librarian at {library.name}: {librarian.name}")
except Library.DoesNotExist:
    print("Library not found.")
except Librarian.DoesNotExist:
    print("Librarian not assigned to this library.")
