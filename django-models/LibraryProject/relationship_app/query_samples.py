import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
print("\n--- Books by a specific author ---")
author = Author.objects.first()
if author:
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    for book in books_by_author:
        print("-", book.title)
else:
    print("No authors found.")

# 2. List all books in a library
print("\n--- Books in a library ---")
library = Library.objects.first()
if library:
    books_in_library = library.books.all()
    print(f"Books in {library.name}:")
    for book in books_in_library:
        print("-", book.title)
else:
    print("No libraries found.")

# 3. Retrieve the librarian for a library
print("\n--- Librarian for a library ---")
if library:
    try:
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library.name} is {librarian.name}")
    except Librarian.DoesNotExist:
        print("No librarian assigned to this library.")
else:
    print("No libraries available to retrieve librarian.")
