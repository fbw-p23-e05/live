from django.http import HttpResponse
from .models import Author, Book, Genre, StoreManager, StoreLocation
from django.views import View
from django.urls import reverse
from django.shortcuts import render


def index(request):
    num_of_books = Book.objects.all().count()
    return render(request, "store/index.html", {"num_of_books": num_of_books})
    

class AuthorListView(View):
    
    def get(self, request):
        # Retrieving the full list of authors as queryset
        authors = Author.objects.all()
        return render(request, "store/author_list.html", {"authors": authors})


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
