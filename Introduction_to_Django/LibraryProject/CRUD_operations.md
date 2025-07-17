# -------------------------------------
# 📘 CREATE
# -------------------------------------
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

book
# Output:
# <Book: Book object (1)>


# -------------------------------------
# 🔍 RETRIEVE
# -------------------------------------
book = Book.objects.get(title="1984")

book.title
# Output: '1984'

book.author
# Output: 'George Orwell'

book.publication_year
# Output: 1949


# -------------------------------------
# ✏️ UPDATE
# -------------------------------------
book.title = "Nineteen Eighty-Four"
book.save()

book.title
# Output: 'Nineteen Eighty-Four'


# -------------------------------------
# ❌ DELETE
# -------------------------------------
book.delete()
# Output: (1, {'bookshelf.Book': 1})

# Confirm deletion
Book.objects.all()
# Output: <QuerySet []>
