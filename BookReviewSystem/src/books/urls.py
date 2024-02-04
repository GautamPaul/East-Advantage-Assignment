from django.urls import path
from books.views import BookReviewView

urlpatterns = [
    path('api/books/<int:id>/review/', BookReviewView.as_view()),
]