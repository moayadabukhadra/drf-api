from django.test import TestCase
from .models import Book
from django.urls import reverse

# Testing the model
class BookTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testbook = Book.objects.create(title = "test_Book", author="admin",description="Testing Book")
        testbook.save()


    def test_books_model_title(self):
        book = Book.objects.get(id=1)
        actual_title = book.title
        self.assertEqual(actual_title, "test_Book")


    def test_books_model_author(self):
        book = Book.objects.get(id=1)
        actual_author=book.author
        self.assertEqual(actual_author, "admin")

    def test_list_page_status_code(self):
        url = reverse('books_list')
        response =self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_status_code(self):
        response=self.client.get('/books/api/v1/1')
        self.assertEqual(response.status_code, 200)

