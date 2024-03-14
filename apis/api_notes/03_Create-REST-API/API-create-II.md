# **5.03 Create REST api**

## **Overview**
This submodule is designed to teach you how to create, secure, validate, sanitize RESTful APIs using Django REST Framework (DRF).

## **Authentication**
- In Django REST Framework (DRF), authentication refers to the process of verifying the identity of a user or client making a request to an API. It is the mechanism used to ensure that only authorized users or clients are allowed to access protected resources.
- When a request is made to an API that requires authentication, DRF checks the credentials provided by the user or client to determine whether the request is authorized. If the credentials are valid, the user or client is considered authenticated and granted access to the protected resource. If the credentials are invalid or missing, the user or client is denied access and an error response is returned.
- Authentication is an important security feature in DRF, as it helps prevent unauthorized access to sensitive resources and data. It is typically implemented alongside authorization, which defines the permissions and privileges that authenticated users or clients have within an API.

Examples of authentication :
1. **Username and password authentication:**

- The built-in `User` model provides a way to store user credentials, including their username and password.
- The `AuthenticationForm`, `UserCreationForm`, and `PasswordResetForm` are built-in Django forms for handling user authentication.

2. **Social media authentication:**

- Django provides several packages for integrating social media authentication into your application, such as `django-allauth` and `django-social-auth`.
- These packages provide integration with various social media providers, as well as authentication views and forms.

3. **Token-based authentication:**

- The `rest_framework.authentication.TokenAuthentication` class in Django Rest Framework provides a simple way to implement token-based authentication in your API.
- The `django-rest-knox` package provides a more advanced implementation of token-based authentication that includes support for token expiry and revocation.

4. **Two-factor authentication:**

- The `django-two-factor-auth` package provides support for implementing two-factor authentication in your Django application.
- This package includes views and forms for handling two-factor authentication, as well as support for various types of two-factor authentication methods.

5. **Biometric authentication:**

- There are several third-party packages available for implementing biometric authentication in Django, such as `django-fido2` and `django-webauthn`.
- These packages provide support for various types of biometric authentication methods, such as fingerprints and facial recognition.


## **Permissions**
Permissions, on the other hand, determine whether a user has the right to perform a certain action within an application. \
Permissions can be used to control access to views, templates, and other resources within an application. Django provides a powerful permission system that allows developers to define custom permissions and assign them to users and user groups.\
 Permissions can be used to restrict access to specific pages or views within an application, and to restrict access to specific data or functionality within the application.\

Django's built-in permissions system has three types of permissions:

- View permissions: Determine whether a user can view a particular object or resource.
- Change permissions: Determine whether a user can modify or update a particular object or resource.
-Delete permissions: Determine whether a user can delete a particular object or resource.
These permissions can be assigned to users or groups, and can be controlled at the model level or at the view level.
Here are some examples of permissions in Django:

1. Object-level permissions:
   - Django provides built-in `ModelBackend` and `ObjectPermissionBackend` backends for implementing object-level permissions.
   - Object-level permissions allow you to restrict access to specific objects based on the user's permissions.
   - For example, you might allow only the owner of a post to edit or delete it.

2. View-level permissions:
   - Django provides the `permissions` attribute on views, which allows you to specify which permissions are required to access a view.
   - View-level permissions allow you to restrict access to entire views based on the user's permissions.
   - For example, you might allow only authenticated users to access a particular view.

3. Custom permissions:
   - Django allows you to define custom permissions by subclassing the built-in `django.contrib.auth.models.Permission` model.
   - Custom permissions allow you to define fine-grained permissions that are specific to your application's needs.
   - For example, you might define a custom permission that allows users to create new posts, but not edit or delete existing ones.

4. Group-based permissions:
   - Django provides built-in support for assigning permissions to groups of users.
   - Group-based permissions allow you to define sets of permissions that can be easily assigned to multiple users at once.
   - For example, you might define a group that has permissions to create and edit posts, and assign that group to all of your content editors.

5. Anonymous user permissions:
   - Django allows you to specify permissions for anonymous users, who are users that are not logged in.
   - Anonymous user permissions allow you to control what actions non-authenticated users can perform.
   - For example, you might allow anonymous users to view public posts, but not create or edit them.

These are just a few examples of the types of permissions that can be implemented in Django. The specific permissions you need for your application will depend on your requirements and the level of access control you need to implement.


In summary, authentication and permission are essential components of web application security, and Django provides robust mechanisms for implementing both.
## Autheticate DRF CRUD app
First, let's add **'rest_framework.authtoken'**  to the **INSTALLED_APPS** list in the **myproject/settings.py** file:

```python 
INSTALLED_APPS = [
    # ... other apps ...
    'rest_framework',
    'rest_framework.authtoken',
    'books',
]
```
 Next, we need to add the **TokenAuthentication** backend to the default authentication backend in the **myproject/settings.py** file:
 ```python
 REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}
```
This means that TokenAuthentication will be the first authentication method that is attempted, followed by SessionAuthentication and BasicAuthentication.\

In **myBookapp/views.py** we want to make the GET requests allowed for everyone, but the POST, PUT, and DELETE requests authenticated.
- In **myBookapp** we create **permissions.py** where we define our permissions
```python 
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly,SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff
```
In Django REST Framework, safe methods are HTTP methods that do not modify the server state. These methods include GET, HEAD, and OPTIONS.
- Next, we need to define the authentication classes that we want to use in the views.py file:
```python 
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics,permissions
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly

class BookList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly ,permissions.IsAuthenticatedOrReadOnly,]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

```
 The views are secured by **TokenAuthentication** and **IsAdminOrReadOnly** permission classes. The **IsAdminOrReadOnly** permission class allows all users to read (**GET** requests) the book data, but only staff members can create, update, or delete (**POST**,**PUT**, and **DELETE** requests) book data.\
 Finally, we need to create a token for each user that wants to access the API. First we create super users by the following command:
 ```console 
 python manage.py createsuperuser
 ```
 In Django Rest Framework (DRF), a **token** is a string of characters that is used to authenticate a user in an API. The token is generated by the server when the user logs in and is returned to the client. The client can then use the token to authenticate future requests to the API.

**Token authentication** is a type of authentication in which a token is used to authenticate a user instead of a username and password. In DRF, the token authentication is implemented using the TokenAuthentication class.
 You can create a token for a user by running the following command in the Django shell:
 ```bash
>>>from django.contrib.auth.models import User
>>>from rest_framework.authtoken.models import Token

>>>user = User.objects.get(username='your_username')
>>>token = Token.objects.create(user=user)
>>>print(token.key)
```
Replace 'your_username' with the username of the user that you want to create a token for. This will print out a long string of characters - this is the token that you can use to authenticate requests to the API.\

Now, when a user wants to access the API, they will need to include their token in the request headers. For example:
```console
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```
We test the authentication by making requests to the API using tools like Postman.