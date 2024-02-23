from django.test import TestCase
from store.models import Book, Author, Genre
from django.urls import reverse


class TestBookListView(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Create an author object
        Author.objects.create(
            first_name="John",
            last_name="Brown",
            email="jbrown@books.com",
            date_of_birth="1954-05-19",
            num_of_books=7
            )
        # create a genre object
        Genre.objects.create(name="Programming")
        
        # Get author and genre objects
        author = Author.objects.get(id=1)
        genre = Genre.objects.get(id=1)
        
        # Create a book object
        Book.objects.create(
            title="Django Test Book",
            author=author,
            summary="A lovely about testing in Django.",
            isbn="1235478945678",
            # genre=genre,
            date_of_publishing="2014-08-15",
            in_stock=True,
            price=85.36,            
        )
        Book.objects.create(
            title="An extra about testing",
            author=author,
            summary="A lovely about testing in Django.",
            isbn="1235478945524",
            # genre=genre,
            date_of_publishing="2014-09-15",
            in_stock=True,
            price=99.24,           
        )
        book = Book.objects.get(id=1)
        book.genre.set((1,))
        book2 = Book.objects.get(id=2)
        book2.genre.set((1,))
        
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/store/books/')
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("store:book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/book_list.html')
        
    def test_list_all_books(self):
        response = self.client.get(reverse("store:book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['books']), 2)
