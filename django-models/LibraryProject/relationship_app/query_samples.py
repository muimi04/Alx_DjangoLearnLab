import os
import django
import sys

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.filter(name="Jane Austen").first()
if author:
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")
else:
    print("Author 'Jane Austen' not found.")

# 2. List all books in a library
library = Library.objects.filter(name="City Library").first()
if library:
    books_in_library = library.books.all()
    print(f"Books in {library.name}: {[book.title for book in books_in_library]}")
else:
    print("Library 'City Library' not found.")

# 3. Retrieve the librarian for a library
if library:
    librarian = Librarian.objects.filter(library=library).first()
    if librarian:
        print(f"Librarian at {library.name}: {librarian.name}")
    else:
        print(f"No librarian found for {library.name}.")
