from pyexpat import model
from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title','author','description')
        model = Book
