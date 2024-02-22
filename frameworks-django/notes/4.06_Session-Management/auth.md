# Implementing Django Auth

1. Create a new Django app within your project:

    ```shell
    cd myproject
    python manage.py startapp user
    ```

2. Configure Django

    Open your Django project’s settings.py file and write the following code :

    ```python
    INSTALLED_APPS = [
        # ...
        # ..
        # .
        # 👇 1. Add this line
        'user',
    ]
    ```


3. Add the URLs

    In this, For accessing our application `user` urls we have to add the following line to the `pytech_bookstore/urls.py` file.

    Open the `urls.py` from inside of your project folder and write the following code:

    ```python
    from django.contrib import admin
    from django.urls import path, include # 👈 1. Add this line

    urlpatterns = [
        # .....
        # 👇 2. Add the app url on this
        path('user/', include('user.urls', namespace="user")),
    ]
    ```
    URL Configuration of views:

    Create a new file `urls.py` inside the `user` folder and write the below code:

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('login/', views.Login.as_view(), name='login'),
        path('register/', views.user_registration, name='register'),
        path('logout/', views.user_logout, name='logout'),
    ]
    ```

    1. `urlpatterns`: This is a list that holds the URL patterns for the application. Each URL pattern is defined as an element in the list.

    2. `path('login/', views.Login.as_view(), name='login')`: This line defines the URL pattern for the login page. The 'login/' string represents the URL path /login/. The views.Login.as_view() specifies that the `Login` class in the views module will handle the logic for rendering the login page. The `name='login'` assigns a name to this URL pattern.

    3. `path('register/', views.user_registration, name='register')`: This line defines the URL pattern for the register page. The 'register/' string represents the URL path `/register/`. The `views.user_registration` specifies that the `user_registration` function in the views module will handle the logic for rendering the register page. The `name='register'` assigns a name to this URL pattern.

    4. `path('logout/', views.user_logout, name='logout')`: This line defines the URL pattern for the logout page. The 'logout/' string represents the URL path `/logout/`. The `views.user_logout` specifies that the `user_logout` function in the views module will handle the logic for rendering the logout page. The `name='logout'` assigns a name to this URL pattern.

    These URL patterns determine the mapping between the URLs entered by the users and the corresponding views that should be rendered.

5. Add the Views

    Open, The `views.py` from `user` folder and write the below code for showing and redirecting to our templates:

    ```python
    from django.shortcuts import render, redirect
    from .forms import RegistrationForm, LoginForm
    from django.views import View
    from django.contrib.auth import authenticate, login, logout


    def user_registration(request):
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            
            if form.is_valid():
                form.save()
                return redirect('/store')
            
        elif request.method == "GET":
            form = RegistrationForm()
            
        return render(request, "user/registration.html", {"form": form})


    class Login(View):
        def get(self, request):
            form = LoginForm()
            return render(request, "user/login.html", {"form": form})
        
        def post(self, request):
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect("/store")
                else:
                    return render(request, "user/login.html", {"form": form})
            else:
                return render(request, "user/login.html", {"form": form})


    def user_logout(request):
        logout(request)
        return redirect('/store')
    ```


    The code snippet you provided represents a Django `views.py` file that includes various views for user authentication and account management. Here’s a breakdown of each function:

    1. `user_registration(request)`: This view handles the registration page. It checks if the request method is POST, which indicates a form submission. If so, it validates the submitted form data using RegistrationForm. If the form is valid, it saves the user and redirects them to the login page. If the request method is GET, it creates a new instance of RegistrationForm and renders the 'registration.html' template, passing the form as context.

    2. `Login(View)`: This view handles the login page. It checks if the request method is POST, indicating a form submission. It validates the submitted form data using `LoginForm`. If the form is valid, it retrieves the username and password from the cleaned data. It then authenticates the user using `authenticate()` and logs them in using `login()`. If the user is successfully authenticated, it redirects them to the home page. If the request method is GET, it creates a new instance of `LoginForm` and renders the 'login.html' template, passing the form as context.

    3. `user_logout(request)`: This view handles the logout functionality. It calls the `logout()` function provided by Django to log out the user and redirects them to the login page.

    The code also includes import statements for various Django modules and forms (render, redirect, authenticate, login, logout, RegistrationForm, and LoginForm). These imports are necessary for the proper functioning of the views.

    Overall, this code demonstrates a basic implementation of user signup, login, and logout functionality using Django, along with the associated forms. You can integrate these views into your Django project to enable user authentication and account management.

6. Forms

    Create a new file `forms.py` inside user folder and write the below code:

    ```python
    from django import forms 
    from django.contrib.auth.models import User
    from django.contrib.auth.forms import UserCreationForm


    class RegistrationForm(UserCreationForm):
        
        class Meta:
            model = User
            fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']


    class LoginForm(forms.Form):
        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)
    ```
        
    The code snippet you provided represents a Django forms module that defines two forms: RegistrationForm and LoginForm. These forms are used for user registration and login functionality in a Django application.

    `RegistrationForm`:

    Inherits from UserCreationForm, which is a built-in Django form specifically designed for user registration.
    The UserCreationForm provides fields for username, password1, and password2 (password confirmation).
    The Meta class specifies the model to be used, which is the default Django User model imported from django.contrib.auth.models.
    The fields attribute lists the fields that should be included in the form, namely 'username', 'first_name', 'last_name', 'password1', 'password2', 'email'.

    `LoginForm`:

    A standard Django form used for user login.
    It does not inherit from any specific Django form class.
    It defines two fields, ‘username’ and ‘password’, using the forms.CharField() method.
    The ‘password’ field is rendered as a password input field due to the widget=forms.PasswordInput argument.
    These forms can be used within Django views to handle user registration and authentication processes. They provide a convenient way to generate HTML forms with appropriate fields and validation.

7. Templates

    Create a new folder templates called `user` and create a new file `login.html` and write the below code:

    ```html
    {% extends "base.html" %}

    {% block content %}
    <div class="content-body">
        <div class="container">
            <div class="row">
                <main class="col-md-12">
                    <h1 class="page-title">Login</h1>
                    <form method="post">
                        {% csrf_token %}
                        {{ form }}
                        <input type="Submit" value="Login">
                    </form>
                </main>
            </div>
        </div>
    </div>
    {% endblock %}
    ```

    Create a new file in the same folder called `registration.html`:

    ```html
    {% extends "base.html" %}

    {% block content %}
    <div class="content-body">
        <div class="container">
            <div class="row">
                <main class="col-md-12">
                    <h1 class="page-title">Register</h1>
                    <form method="post">
                        {% csrf_token %}
                        {{ form }}
                        <input type="Submit" value="Save">
                    </form>
                </main>
            </div>
        </div>
    </div>
    {% endblock %}
    ```