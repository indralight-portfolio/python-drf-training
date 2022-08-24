from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .serializers import BookSerializer
from .models import Book


@api_view(["GET"])
def HelloAPI(request):
    return Response("hello world")


class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
