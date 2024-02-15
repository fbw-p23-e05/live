from django.http import HttpResponse
from .models import Author, Book, Genre, StoreManager, StoreLocation
from django.views import View
from django.urls import reverse


def index(request):
    authors_link = f"<a href={reverse('store:author_list')}>Authors</a>"
    books_link = f"<a href={reverse('store:book_list')}>Books</a>"
    genres_link = f"<a href={reverse('store:genre_list')}>Genres</a>"
    
    content = f"<ul>{authors_link} {books_link} {genres_link}</ul>"
    return HttpResponse(content)
    

class AuthorListView(View):
    
    def get(self, request):
        # Retrieving the full list of authors as queryset
        authors = Author.objects.all()
        
        # Initialize the content variable
        content = ""
        
        # Loop over the authors queryset
        for author in authors:
            # Create a HTML list element that includes each authors names
            new_author = f"<li>{author}</li>"
            # append the HTML element to content
            content += new_author
            
        return HttpResponse(content)


class BookListView(View):
    
    def get(self, request):
        books = Book.objects.all()
        content = ""
        
        for book in books:
            new_book = f"<li>{book} - {book.author}</li>"
            content += new_book
            
        return HttpResponse(content)
    

class GenreListView(View):
    
    def get(self, request):
        genres = Genre.objects.all()
        content = ""
        
        for genre in genres:
            new_genre = f"<li>{genre}</li>"
            content += new_genre
            
        return HttpResponse(content)
