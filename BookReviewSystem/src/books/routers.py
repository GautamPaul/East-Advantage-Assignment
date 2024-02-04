from rest_framework import routers
from books.viewsets import BooksViewSet, ReviewViewSet


app_name = "books"

router = routers.DefaultRouter()
router.register("books", BooksViewSet)
router.register("reviews", ReviewViewSet)