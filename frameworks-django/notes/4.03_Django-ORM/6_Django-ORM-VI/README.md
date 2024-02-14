# Django ORM VI

## Understanding the concepts of Eager and Lazy Loading and how these concepts are implemented in the QuerySet

### What is Eager and Lazy Loading?
- Eager loading is when related data is loaded from the database all at once, in a single query, along with the main object that you are querying. 
- Lazy loading is when related data is only loaded when it is actually accessed in your code, typically resulting in multiple queries to the database.

### Why do we need to understand Eager and Lazy Loading?
- Understanding these concepts can help improve the performance of your Django application, particularly when dealing with large datasets and complex relationships between your database models.

### Where are these concepts used in Django?
- These concepts are used in Django's QuerySet API, which allows you to easily query your database and retrieve data.

### How are these concepts implemented in the QuerySet?
- By default, Django uses lazy loading for related objects in QuerySets. This means that when you access a related object on a QuerySet, Django will issue another query to the database to fetch the related data.
- You can use the `select_related` method to specify related fields that should be eagerly loaded when the QuerySet is evaluated. For example:

```python
# Using select_related to eagerly load related objects
from myapp.models import Book

books = Book.objects.select_related('author').all()

for book in books:
    print(book.author.name)
```

- This code will fetch all `Book` objects from the database and eagerly load the related `Author` object for each book, allowing us to access the author's name without issuing additional queries.

- You can also use the `prefetch_related` method to specify related fields that should be loaded in a separate query, but still more efficiently than lazy loading. For example:

```python
# Using prefetch_related to efficiently load related objects
from myapp.models import Book

books = Book.objects.prefetch_related('reviews').all()

for book in books:
    print(f"Book: {book.title}")
    for review in book.reviews.all():
        print(f" - {review.text}")
```

- This code will fetch all `Book` objects from the database, and will prefetch the related `Review` objects for each book in a separate query. This allows us to access the reviews for each book without issuing additional queries for each book.

## Know how to configure and use the Django Admin Webpage

### What is the Django Admin Webpage?
- The Django Admin Webpage is a built-in web-based interface that allows you to easily manage your Django application's data and settings.

### Why do we need to know how to configure and use it?
- The Django Admin Webpage is a powerful tool for managing your application, and can save you a lot of time when dealing with routine tasks such as adding or updating data.

### Where do we find the Django Admin Webpage?
- You can access the Django Admin Webpage by navigating to `/admin` on your application's domain, provided that you have set up the Django admin site correctly.

### How do we configure and use it?
- To configure the Django Admin Webpage, you need to define "Admin" classes in your application's `admin.py` file. Here's an example:

```python
# Creating an Admin class for our Book model
from django.contrib import admin
from myapp.models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
```

- In this code, we define an `Admin` class for our `Book` model, and register it using the `admin.register` decorator. We also specify that the `title`, `author`, and `published_date` fields should be displayed in the list view of the `Book` model in the Django Admin Webpage.

- Once you have defined your Admin classes, you can access the Django Admin Webpage by navigating to `/admin` on your application's domain, and logging in with an account that has been granted staff status.

- From the Django Admin Webpage, you can perform a wide range of tasks, including creating, updating, and deleting database objects, managing user accounts and groups, and configuring settings for your application.

- For example, if we had defined an `Admin` class for our `Book` model as shown above, we would see a list of all `Book` objects in the Django Admin Webpage, and could perform actions such as adding a new `Book`, editing an existing `Book`, or deleting a `Book`.

- The Django Admin Webpage also provides a powerful search and filtering interface, allowing you to quickly find the data you need. You can also customize the look and feel of the Django Admin Webpage by creating custom templates and static files in your application's `templates/admin` and `static/admin` directories, respectively.


- In addition to the default functionality provided by the Django Admin Webpage, you can also extend and customize it by creating custom views and forms, or by using third-party packages such as `django-admin-tools` or `grappelli`.

- For example, you could create a custom view to display statistics or reports about your application's data, or a custom form to provide a more user-friendly interface for adding or updating objects.

- Overall, the Django Admin Webpage is a powerful and flexible tool for managing your application's data and settings, and understanding how to configure and use it is an important skill for any Django developer.

