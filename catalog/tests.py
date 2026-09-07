from django.test import TestCase
from django.urls import reverse

from .models import Publisher, Book, Review

# Create your tests here.

#Tests the ability to create and destroy database objects
class BookListViewTests(TestCase):
    def setUp(self):
        self.publisher = Publisher.objects.create(name="Test Publisher")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            publisher=self.publisher,
        )
        self.review = Review.objects.create(
            body="Example Review",
            book=self.book,
        )

    def test_publisher_str(self):
        self.assertIn("Test Publisher", str(self.publisher))

    def test_book_str(self):
        self.assertIn("Test Book", str(self.book))

    def test_review_str(self):
        self.assertIn("Test Book", str(self.review))

    def test_book_appears_on_books_page(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)

