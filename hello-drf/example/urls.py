from django.urls import path, include
from .views import BooksAPI, BookAPI, HelloAPI

urlpatterns = [
    path("hello/", HelloAPI),
    path("books/", BooksAPI.as_view()),
    path("book/<int:bid>", BookAPI.as_view()),
]
