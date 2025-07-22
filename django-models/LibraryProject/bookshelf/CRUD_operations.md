# CRUD Operations for Book Model in Django Shell

## 1. Create a Book Instance

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
 
## 2.  Retrieve the Book Instance
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

## 3. Update the Book Title
book.title = "Nineteen Eighty-Four"
book.save()

## 4. Delete the Book Instance
book.delete()
Book.objects.all()
