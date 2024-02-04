import datetime
from django.db import models


YEAR_CHOICES = [(year, year) for year in range(1975, datetime.date.today().year+1)]
default_year = datetime.datetime.now().year
RATING_CHOICES = [(rating, rating) for rating in range(1,6)]

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=default_year, choices=YEAR_CHOICES)

    def __str__(self):
        return f"{self.title}"


class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField(default=3, choices=RATING_CHOICES)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"{self.book.title}'s Review"