from django.test import TestCase

from django.test import TestCase
from .models import Author, Book
from datetime import date

class AuthorModelTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='John Doe', bio='A famous author')

    def test_author_name(self):
        self.assertEqual(self.author.name, 'John Doe')

    def test_author_bio(self):
        self.assertEqual(self.author.bio, 'A famous author')

    def test_author_string_representation(self):
        self.assertEqual(str(self.author), 'John Doe')

class BookModelTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='John Doe', bio='A famous author')
        self.book = Book.objects.create(
            title='Book Title',
            description='Description of the book',
            publication_date=date.today(),
            cover_image='book_covers/cover.jpg',
            price=19.99
        )
        self.book.authors.add(self.author)

    def test_book_title(self):
        self.assertEqual(self.book.title, 'Book Title')

    def test_book_description(self):
        self.assertEqual(self.book.description, 'Description of the book')

    def test_book_publication_date(self):
        self.assertEqual(self.book.publication_date, date.today())

    def test_book_price(self):
        self.assertEqual(self.book.price, 19.99)

    def test_book_authors(self):
        self.assertEqual(list(self.book.authors.all()), [self.author])

    def test_book_string_representation(self):
        self.assertEqual(str(self.book), 'Book Title')