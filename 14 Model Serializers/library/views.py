from django.shortcuts import render
from rest_framework import generics
from .models import Author, Category, Book
from .serializers import AuthorSerializer, CategorySerializer, BookSerializer, BookHyprelinkedSerializer
# Create your views here.

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookListCreateView(generics.ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AvailableBooksView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(available=True)

class BooksByCategoryView(generics.ListAPIView):

    serializer_class = BookSerializer

    def get_queryset(self):
        category = self.kwargs['name']

        return Book.objects.filter(category__name__iexact=category)


class BookHyperlinkedView(generics.ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookHyprelinkedSerializer


from rest_framework.response import Response
class BookListCreateView(
        generics.ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()

        serializer = self.get_serializer(
            queryset,
            many=True
        )

        return Response({
            'total_books': queryset.count(),
            'books': serializer.data
        })
