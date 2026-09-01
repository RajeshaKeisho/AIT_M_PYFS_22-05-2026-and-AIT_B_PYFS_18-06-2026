from rest_framework import serializers
from .models import Author, Category, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Book
        fields = [
            'id','title', 'price', 'published_date', 'available', 'author', 'author_name', 'category', 'category_name'
        ]


class BookHyprelinkedSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name="author-detail", read_only=True)
    category = serializers.HyperlinkedRelatedField(view_name="category-detail", read_only=True)

    class Meta:
        model = Book
        fields = [
            'url', 'id', 'title', 'price', 'published_date', 'available', 'author', 'category'
        ]

