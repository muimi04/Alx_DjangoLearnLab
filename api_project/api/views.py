from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# ListAPIView for simple listing
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ViewSet for full CRUD functionality
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
