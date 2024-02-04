from rest_framework import viewsets
from books.models import Book, Review
from books.serializers import BookSerializer, ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'publication_year']


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer