# Creating REST APIs with Django and Django Rest Framework (DRF)

- Django Rest Framework and integrate into Django
- Serialization and Deserialization
- How to write serializers
- Using Views and Viewsets

1. Create and activate a virtual environment

    python3 -m venv .api_venv
    source .api_venv/bin activate

2. Install django and DRF

    pip install django djangorestframework

3. Create a Django project

    django-admin startproject myproject .

4. Create a Django app

    django-admin startapp todo

5. add app to the settings.py

    "rest_framework",
    "todo.apps.TodoConfig",

**Main DRF components:**

- Serializers - are used to convert Querysets and model instances to(serialization) and from(deserialization) JSON.
- Views - similar to traditional Django Views, handle RESTful HTTP requests and responses. The views themselves use serializers to validate incoming payloads and contain the necessary logic to return a response. 
> Payload - data that is sent from the API. (POST, PUT, PATCH, DELETE)

6. Create a model in models.py

    ```python
    class Task(models.Model):
        title = models.CharField(max_length=200)
        description = models.TextField()
        completed = models.BooleanField(default=False)
    ```

7. create a file called serializers.py:

    ```python
    from rest_framework import serializers
    from .models import Task

    # basic serializer
    class TaskSerializer(serializers.Serializer):
        title = serializers.CharField()
        description = serializers.CharField()
        completed = serializers.BooleanField()

    # OR

    # model Serializer
    class TaskSerializer(serializers.ModelSerializer):
        class Meta:
            model = Task
            fields = "__all__"
    ```

**Views and Viewsets**

- Change incoming requests to request instances
- Handle authentication and authorization
- Perform CRUD actions (Create, Read(List, Retrieve), Update, Delete(Destroy))
- return a response object.

Types of DRF views:
- APIView
- Viewset
- Generic View

## APIView

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Task


class ListTasks(APIView):

    # 1. List all tasks
    def get(self, request, *args, **kwargs):
        """List all todo items."""
        # getting a list of all tasks
        tasks = Task.objects.filter(completed=False)
        # feed all tasks into serializer
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 2. Create a task
    def post(self, request, *args, **kwargs):
        """Create a todo with the given payload."""
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

Create urls.py file in the todo app folder and the following code:

```python
from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.ListTasks.as_view(), name="task_list"),
]
```

Include the urls.py from todo app in the main urls.py file:

```python
from django.urls import include

urlpatterns = [
    # ....
    path("api/todo/", include("todo.urls", namespace="todo")),
]
```

> create and run migrations before launching the development server.

## Generic View

https://www.django-rest-framework.org/api-guide/generic-views/

- Handle Common use cases without much friction

```python
from rest_framework.generics import ListCreateAPIView

class ListTasks(ListCreateAPIView):
    queryset = Task.objects.filter(completed=False)
    serializer_class = TaskSerializer
```

Create urls.py file in the todo app folder and the following code:

```python
from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.ListTasks.as_view(), name="task_list"),
]
```

Include the urls.py from todo app in the main urls.py file:

```python
from django.urls import include

urlpatterns = [
    # ....
    path("api/todo/", include("todo.urls", namespace="todo")),
]
```

> create and run migrations before launching the development server.

## Viewsets

https://www.django-rest-framework.org/api-guide/viewsets/

```python
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404

class TaskViewSet(ViewSet):

    def list(self, request):
        """Listing all the task objects."""
        queryset = Task.objects.filter(completed=False)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Get a particular object."""
        queryset = Task.objects.filter(completed=False)
        task = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

```

Add the urls to the todo/urls.py file:

```python
urlpatterns =[
    # .....
    path("all/", views.TaskViewSet.as_view(), name="all_tasks"),
    path("<int:pk>/", views.TaskViewSet.as_view(), name="retrieve_task"),
]
```

## Authentication

- security concerns
- Adding authentication:
    - BasicAuthentication
    - TokenAuthentication
- sanitization and validation.

**BasicAuthenticaton:**

1. Add the authentications defaults to settings.py:

    ```python
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.BasicAuthentication',
        ]
    }
    ```

2. Add permission classes to API Views

    ```python
    from rest_framework.permissions import IsAuthenticated

    # add permissions to specific views 
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]
    ```

2. create a user to test with

    ```
    python manage.py createsuperuser
    ```

3. Test our APIs with Postman

4. A basic to specific APIss:

    ```python
    from rest_framework.authentication import BasicAuthentication

    # add API level auth
    authentication_classes = [BasicAuthentication]
    ```

**TokenAuthentication:**

1. Activating the authtoken in settings.py:

    ```python
    INSTALLED_APPS = [
        # .... other apps
        'rest_framework.authtoken',
    ]

1. add the settings

    ```python
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            # ....
            'rest_framework.authentication.TokenAuthentication',
        ]
    }

2. create a endpoint to generate an authentication token in todo/urls.py:

    ```python
    from rest_framework.authtoken.views import obtain_auth_token

    urlpatterns = [
        # ...some other paths
        path('auth-token/', obtain_auth_token, name="api_auth_token"),
    ]
    ```

3. Run migrations to create authtoken table in the DB:

    python manage.py makemigrations
    python manage.py migrate

3. generate the apitoken

4. test the authentication using postman


## Authorization 

- restricting access using permission classes

1. create a blog app

    django-admin startapp blog

2. Activate the blog app in settings.py

    ```python
    INSTALLED_APPS = [
        # ... other apps
        'blog.apps.BlogConfig',
    ]
    ```

3. Create a BlogPost model:

    ```python
    from django.utils.text import slugify

    class BlogPost(models.Model):
        title = models.CharField(max_length=200)
        body = models.TextField()
        published_on = models.DateTimeField(auto_now_add=True)
        slug = models.SlugField()
        category = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title))
        super(BlogPost, self).save(*args, **kwargs)
    ```

4. Create a serializer.py file and add a serializer for the BlogPost model:

    ```python
    from rest_framework import serializers
    from .models import BlogPost

    class BlogPostSerializer(serializers.ModelSerializer):
        class Meta:
            model = BlogPost
            exclude = ['slug', 'published_on']
    ```


5. Create a generic views for the BlogPost.

    ```python
    from django.shortcuts import render
    from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
    from .serializers import BlogPostSerializer
    from .models import BlogPost


    class PostListView(ListCreateAPIView):
        """Get a list of all posts
        Create new posts.
        """
        queryset = BlogPost.objects.all()
        serializer_class = BlogPostSerializer
        
        
    class PostDetailView(RetrieveUpdateAPIView):
        """Retrieve a specific post.
        Update that post.
        """
        queryset = BlogPost.objects.all()
        serializer_class = BlogPostSerializer
    ```

6. Add permissions to restrict access

7. Create endpoints for the view

    ```python
    # blog/urls.py
    from django.urls import path
    from . import views

    app_name = "blog"

    urlpatterns = [
        path("", views.PostListView.as_view(), name="post_list"),
        path("<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    ]


    #myproject/urls.

    urlpatterns = [
        path('api/blog/', include("blog.urls", namespace="blog")),
    ]
    ```

8. Create migrations and migrate:

    python manage.py makemigrations
    python manage.py migrate

9. Test our endpoints using Postman

## Sanitization

1. Install django html sanitizer:

    pip install django-html_sanitizer

2. Add to installed apps in settings.py:

    ```python
    INSTALLED_APPS = [
        # other apps
        "sanitizer",
    ]
    ```

3. Modify the BlogPost model to use sanitized fields:

    ```python 
    from django.db import models
    from django.utils.text import slugify
    from sanitizer.models import SanitizedTextField # add this


    class BlogPost(models.Model):
        title = models.CharField(max_length=200)
        body = SanitizedTextField(allowed_tags=['a', 'img', 'p'], allowed_attributes=['href', 'src', 'class']) # add this
        published_on = models.DateTimeField(auto_now_add=True)
        slug = models.SlugField()
        category = models.CharField(max_length=50)

        def save(self, *args, **kwargs):
            self.slug = slugify(str(self.title))
            super(BlogPost, self).save(*args, **kwargs)
    ```

4. modify settings.py and the following:

    ```python
    import django
    from pathlib import Path
    from django.utils.encoding import smart_str
    django.utils.encoding.smart_text = smart_str
    ```

## Error Handling

- Using the try except block
- Response messages for errors.

1. edit the blog/views.py and replace the PostDetailView with the following code:

    ```python
    from rest_framework import status
    from rest_framework.response import Response
    from rest_framework.views import APIView

    class PostDetailView(APIView):

        def __get_object(self, post_id):
            """
            Helper method to get a specific object.
            """
            try:
                return BlogPost.objects.get(id=post_id)
            except BlogPost.DoesNotExist:
                return None

        def get(self, request, post_id, *args, **kwargs):
            """Retrieves a specific blog post."""
            blog_post = self.__get_object(post_id)

            if not blog_post:
                message = {"response": f"Blog post with ID #{post_id} does not exist."}
                return Response(message, status=status.HTTP_404_NOT_FOUND)
            
            # if blog post exists create a serializer object
            serializer = BlogPostSerializer(blog_post)
            return Response(serializer.data, status=status.HTTP_200_OK)

        def put(self, request, post_id, *args, **kwargs):
            """
            Update a blog post.
            """
            blog_post = self.__get_object(post_id)
            if not blog_post:
                message = {"response": f"Blog post with ID #{post_id} does not exist."}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

            serializer = BlogPostSerializer(instance=blog_post, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, post_id, *args, **kwargs):
        """Deletes an object given the todo_id"""
            # Retrieve object
            blog_post = self.get_object(post_id)
            if not blog_post:
                return Response({"response": f"Object with ID #{post_id} does not exist."},
                                status=status.HTTP_400_BAD_REQUEST)
                
            # Delete object if it it exists
            blog_post.delete()
            return Response({"message": "Object successfully deleted!"}, status=status.HTTP_204_NO_CONTENT)
    ```