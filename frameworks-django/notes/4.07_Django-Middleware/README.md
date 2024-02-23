# Django Middleware

## Understanding Middleware in Django

### What is Middleware in Django?

Middleware is a Django concept that lets you process requests and responses in the Django framework. Middleware acts as a bridge between a client's request and the server's response. It can intercept requests and responses to modify or enhance them as necessary.

### Why do we need Middleware?

Middleware is useful when you need to perform some tasks or processing before a view function gets executed or after it's done. It can handle tasks such as authentication, CSRF protection, and caching.

### Where to find Built-in Middleware in Django?

Django comes with several built-in middleware that you can use, and they can be found in the `settings.py` file of your Django project under the `MIDDLEWARE` key. 

Here's an example:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
These built-in middleware perform various tasks such as security checks, handling sessions, authentication, and more.

## How to Activate and Deactivate Middleware in Django?

You can activate and deactivate middleware in the `settings.py` file of your Django project by adding or removing the middleware from the `MIDDLEWARE` key list. Here's an example of how to deactivate the CSRF middleware:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
In this example, we have removed the `django.middleware.csrf.CsrfViewMiddleware` middleware from the list.

## How to Implement Custom Class-Based Middleware in Django?

To create a custom middleware, you need to create a new class that inherits from `object`. The class must define the following methods:
* `__init__(self, get_response)` - The constructor method that initializes the middleware.
* `__call__(self, request)` - This method is called for each request and can modify the request or perform some task before the view function gets executed.
* `process_response(self, request, response)` - This method is called after the view function has returned and can modify the response or perform some task after the view function has executed.

Here's an example of how to create a custom middleware that adds a header to every response:

```python
class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Frame-Options'] = 'SAMEORIGIN'
        return response

    def process_response(self, request, response):
        return response
```

Once you have created the custom middleware, you need to add it to the `MIDDLEWARE` list in the `settings.py` file.

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'path.to.CustomHeaderMiddleware',
]
```

In this example, we have added the `CustomHeaderMiddleware` to the end of the `MIDDLEWARE` list. This ensures that it gets executed after all the built-in middleware.

### To summarize:

Middleware in Django is a useful feature that lets you process requests and responses. It can handle tasks such as authentication, CSRF protection, and caching. Django comes with several built-in middleware that you can use, and you can activate or deactivate them by adding or removing them from the `MIDDLEWARE` list in the `settings.py` file. You can also create custom middleware by creating a new class that inherits from `object` and defining the necessary methods, then adding it to the `MIDDLEWARE` list.

