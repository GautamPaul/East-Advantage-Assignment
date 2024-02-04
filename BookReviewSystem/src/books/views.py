import json
from django.views import View
from django.http import JsonResponse
from django.core.serializers import serialize
from books.models import Book, Review
from books.serializers import ReviewSerializer


class BookReviewView(View):
    def get(self, request, id):
        reviews = Review.objects.filter(book=id)
        data = json.loads(serialize("json", reviews, fields=("review", "rating")))
        return JsonResponse({"reviews": data})