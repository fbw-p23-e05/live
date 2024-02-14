from django.contrib import admin
# import the models
from .models import Author, Genre, Book, StoreLocation, StoreManager

# Register your models here.
# admin.site.register(Author)
# admin.site.register(Book)
admin.site.register(Genre)
# admin.site.register(StoreLocation)
# admin.site.register(StoreManager)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_of_birth',)
    list_display_links = ('first_name', 'last_name', 'email')
    ordering = ['first_name', 'last_name']
    fieldsets = [
        ('Names', {
            'fields': (('first_name', 'last_name',), )
        }),
        ('Contact', {
            'fields': ('email',)
        }),
        ('Miscellaneous', {
            'fields': ('date_of_birth', 'num_of_books')
        })
    ]
    
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_of_publishing', 'price',)
    list_filter = ('author', 'date_of_publishing', 'in_stock')
    fields = [
        'title', 'author', 'summary', 'isbn',
        'genre', 'date_of_publishing',
        ('price', 'in_stock')
        ] 
    

class StoreLocationInline(admin.TabularInline):
    model = StoreLocation


@admin.register(StoreManager)
class StoreManagerAdmin(admin.ModelAdmin):
    inlines = [StoreLocationInline]
