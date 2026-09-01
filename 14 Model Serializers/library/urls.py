from django.urls import path

from .views import *

urlpatterns = [

    path(
        'authors/',
        AuthorListCreateView.as_view(),
        name='author-list'
    ),

    path(
        'authors/<int:pk>/',
        AuthorRetrieveUpdateDeleteView.as_view(),
        name='author-detail'
    ),

    path(
        'categories/',
        CategoryListCreateView.as_view(),
        name='category-list'
    ),

    path(
        'categories/<int:pk>/',
        CategoryRetrieveUpdateDeleteView.as_view(),
        name='category-detail'
    ),

    path(
        'books/',
        BookListCreateView.as_view(),
        name='book-list'
    ),

    path(
        'books/<int:pk>/',
        BookRetrieveUpdateDeleteView.as_view(),
        name='book-detail'
    ),

    path(
        'books/available/',
        AvailableBooksView.as_view()
    ),

    path(
        'books/category/<str:name>/',
        BooksByCategoryView.as_view()
    ),

    path(
        'hyper-books/',
        BookHyperlinkedView.as_view()
    ),


]