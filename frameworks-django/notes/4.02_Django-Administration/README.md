# Django Admin CLI

## Using the `manage.py` script

In a Django project, you can use the `manage.py` script to perform various tasks, such as running the development server, creating database tables, and running tests. To use the `manage.py` script, open a command prompt or terminal window, navigate to the directory where your Django project is located, and type `python manage.py` followed by the command you want to run.

### Example:
To start the development server, run `python manage.py runserver` in the command prompt. The output will show the URL to access your Django project in a web browser.

### Why: 
`manage.py` is a powerful tool in a Django project, allowing you to perform various operations with ease. It saves you from writing lengthy command-line arguments and takes care of project-level operations such as creating database tables and migrations.

### Where:
You can find the `manage.py` script in the root directory of a Django project.

### How:
Open a command prompt or terminal window, navigate to the directory where your Django project is located, and type `python manage.py` followed by the command you want to run.

## Understanding Django app and project

A Django project is a collection of settings and configurations for a specific website, while a Django app is a module that houses related functionality such as models, views, and templates. A project can contain multiple apps, and an app can be reused in multiple projects. When you create a new Django project, it automatically comes with a single app called `main`.

### Example:
Let's say you want to create a website to manage your library's books. You can create a Django project called `library_project`, which will contain multiple apps such as `book_management`, `user_management`, and `order_management`.

### Why:
Understanding the difference between a Django project and app is crucial to organizing your code and ensuring reusability. You can also easily share an app between different projects, reducing the amount of code you need to write.

### Where:
A Django project and its apps are typically located in the same directory, with the project in the root directory and apps in subdirectories.

### How:
To create a new Django project, run `django-admin startproject project_name` in the command prompt. To create a new app within a project, run `python manage.py startapp app_name` in the command prompt.

## Generating and applying migrations

In Django, migrations are used to manage changes to your database schema. When you make changes to your models, you create a new migration file that describes those changes. You can then apply the migration to update the database schema. 

### Example:
Let's say you want to add a new field to your `Book` model in the `book_management` app. You can create a new migration by running `python manage.py makemigrations book_management`, which will generate a new migration file in the `book_management/migrations` directory. You can then apply the migration by running `python manage.py migrate book_management`, which will update the database schema.

### Why:
Migrations are a critical aspect of database management in Django. They allow you to make changes to your database schema without losing data and keep your database schema in sync with your models.

### Where:
Migration files are located in the `migrations` directory of an app.

### How:
To create a new migration file, run `python manage.py makemigrations app_name` in the command prompt. To apply the migration, run `python manage.py migrate app_name` in the command prompt.

## Understanding URL mappings to Views in urls.py

In Django, the URLConf system maps URLs to view functions. The `urls.py` file in each app defines the URL patterns that the app handles. Each URL pattern is associated with a specific view function that will be executed when a user visits that URL. The view function typically returns an HTTP response, which is then displayed to the user in their web browser.

### Example:
Let's say you have a `book_management` app that has a `views.py` file with a `list_books` function that returns a list of books. You can map the URL `/books/` to the `list_books` function by adding the following code to `book_management/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='book_list'),
]
```

Now when a user visits `/books/` in their web browser, the `list_books` function will be executed, and the list of books will be displayed.

### Why:
The URLConf system is a critical part of any Django app, as it allows you to map URLs to specific views and create a user-friendly web interface.

### Where:
The `urls.py` file is typically located in each app's directory.

### How:
To map a URL to a view function, add a new `path` to the `urlpatterns` list in the app's `urls.py` file. The `path` function takes two arguments: the URL pattern to match and the view function to execute.

Additionally, you can also use regular expressions to match complex URL patterns, as well as pass parameters from the URL to the view function.

### Example:
Let's say you have a `book_management` app with a `detail_book` function that takes a book ID as a parameter and returns details about that book. You can map URLs like `/books/1/`, `/books/2/`, etc., to the `detail_book` function by adding the following code to `book_management/urls.py`:

```python
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='book_list'),
    re_path(r'^books/(?P<book_id>[0-9]+)/$', views.detail_book, name='book_detail'),
]
```

The `re_path` function uses a regular expression to match URLs that start with `/books/` followed by a book ID, which is passed as a named parameter to the `detail_book` function.

### Why:
Using regular expressions and passing parameters from the URL to the view function allows you to create dynamic, flexible URLs that can handle complex queries and user input.

### Where:
Regular expressions and parameter passing can be used in the `urls.py` file of any Django app.

### How:
To use regular expressions in a URL pattern, use the `re_path` function instead of `path` and specify a regular expression pattern as the first argument. To pass parameters from the URL to the view function, enclose them in angle brackets and give them a name, then include them in the view function's parameters. For example, `(?P<book_id>[0-9]+)` matches one or more digits and passes them to the view function as the `book_id` parameter.

