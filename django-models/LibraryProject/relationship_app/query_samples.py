import os
import django
import sys

# Add the path to your project
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../LibraryProject')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()


from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.get(name="Jane Austen")
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

# 2. List all books in a library
library = Library.objects.get(name="City Library")
books_in_library = library.books.all()
print(f"Books in {library.name}: {[book.title for book in books_in_library]}")

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian at {library.name}: {librarian.name}")
