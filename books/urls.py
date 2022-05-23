from django.urls import path
from books.api.viewset import (
                                BooksListAPIView,
                                BooksDetailAPIView
                                )

urlpatterns = [
    path('api/v1/books-list', BooksListAPIView.as_view(), name='books_list'),
    path('api/v1/<int:pk>', BooksDetailAPIView.as_view(), name='book_detail'),

]