# Django Web Framework

1. Create a virtual environment
    ```shell
    python3 -m venv .venv
    ```

2. Install Django using pip
    ```shell
    pip install Django
    ```

3. Start a Django project
    ```shell
    django-admin startproject art_gallery .
    ```
    Let’s look at what startproject created:

    These files are:

    * ` manage.py`: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about `manage.py` in [django-admin and `manage.py`](https://docs.djangoproject.com/en/5.0/ref/django-admin/).
    * The inner art_gallery/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. art_gallery.urls).
    * `art_gallery/__init__.py`: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, [read more about packages](https://docs.python.org/3/tutorial/modules.html#tut-packages) in the official Python docs.
    * `art_gallery/settings.py`: Settings/configuration for this Django project. [Django settings](https://docs.djangoproject.com/en/5.0/topics/settings/) will tell you all about how settings work.
    * `art_gallery/urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in [URL dispatcher](https://docs.djangoproject.com/en/5.0/topics/http/urls/).
    * `art_gallery/asgi.py`: An entry-point for ASGI-compatible web servers to serve your project. See [How to deploy with ASGI](https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/) for more details.
    * `art_gallery/wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project. See [How to deploy with WSGI](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/) for more details.

    ## Project settings

    There are several settings that Django includes in this file, but these are only part of all the Django settings available. You can see all the settings and their default values at [`https://docs.djangoproject.com/en/5.0/ref/settings/`](https://docs.djangoproject.com/en/5.0/ref/settings/).

    The following settings are worth looking at:

    * `DEBUG` is a Boolean that turns the debug mode of the project on and off. If it is set to `True`, Django will display detailed error pages when an uncaught exception is thrown by your application. When you move to a production environment, remember that you have to set it to `False`. Never deploy a site into production with DEBUG turned on because you will expose sensitive
    project-related data.
    * `ALLOWED_HOSTS` is not applied while debug mode is on or when the tests are run. Once you move your site to production and set `DEBUG` to `False`, you will have to add your domain/host to this setting in order to allow it to serve your Django site.
    * `INSTALLED_APPS` is a setting you will have to edit for all projects. This setting tells Django which applications are active for this site. By default, Django includes the following applications:
        * `django.contrib.admin`: An administration site
        * `django.contrib.auth`: An authentication framework
        * `django.contrib.contenttypes`: A framework for handling content types
        * `django.contrib.sessions`: A session framework
        * `django.contrib.messages`: A messaging framework
        * `django.contrib.staticfiles`: A framework for managing static files
    * `MIDDLEWARE` is a list that contains middleware to be executed.
    * `ROOT_URLCONF` indicates the Python module where the root URL patterns of your application are defined.
    * `DATABASES` is a dictionary that contains the settings for all the databases to be used in the project. There must always be a default database. **The default configuration uses an SQLite3 database.**
    * `LANGUAGE_CODE` defines the default language code for this Django site.
    * `USE_TZ` tells Django to activate/deactivate timezone support. Django comes with support for timezone-aware datetime. This setting is set to True when you create a new project using the `startproject` management command.

4. Start a Django App
    ```shell
    django-admin startapp stock
    ```

    These files are as follows:

    * `admin.py`: This is where you register models to include them in the Django administration site—using this site is optional.
    * `apps.py`: This includes the main configuration of the blog application.
    * `migrations`: This directory will contain database migrations of your application. Migrations allow Django to track your model changes and synchronize the database accordingly.
    * `models.py`: This includes the data models of your application; all Django applications need to have a models.py file, but this file can be left empty.
    * `tests.py`: This is where you can add tests for your application.
    * `views.py`: The logic of your application goes here; each view receives an HTTP request, processes it, and returns a response.

5. Run the development server
    ```shell
    python manage.py runserver
    ```