# **5.03 Create REST api**

## **Overview**
This submodule is designed to teach you how to create and work with swagger/openAPI documentation. 

**keywords :**
(API documentation, API schema, API specification, API versioning, Code generation, Customization, Descriptions, Endpoints, HTTP methods, JSON Schema, Metadata, Parameters, Request/response models, ReDoc, RESTful API, Responses, Schemas, Swagger UI, YAML format.)

## **Swagger/openAPI documentation**
By using **Swagger**, **OpenAPI**, and **ReDoc** documentation in Django REST Framework, you can easily create comprehensive and user-friendly API documentation for your RESTful web services. This can help developers understand and interact with your API more easily, leading to better adoption and usage of your service.

- Swagger: Swagger is an open-source tool used to generate interactive API documentation for RESTful web services. It allows developers to describe the structure of their APIs using a YAML or JSON file, which is then used to generate a user-friendly interface for interacting with the API. In Django REST Framework, Swagger documentation can be generated using the drf_yasg package.

- OpenAPI: OpenAPI is a specification for building APIs. It was formerly known as Swagger and was renamed in 2015. The OpenAPI specification provides a way for developers to describe the structure of their APIs using a YAML or JSON file. This file can then be used to generate documentation, client SDKs, and server stubs. The OpenAPI specification is widely adopted in the industry and is supported by a large number of tools and frameworks.

- ReDoc: ReDoc is an open-source tool used to generate beautiful and responsive API documentation from OpenAPI/Swagger 2.0 and 3.0 specifications. It provides a simple and elegant way to present API documentation to developers, making it easy for them to understand and work with your API. In Django REST Framework, ReDoc documentation can be generated using the drf-yasg package.

1. To implement **Swagger** and **OpenAPI** documentation in our DRF application we must first install **drf_yasg** package by running the folliwing command
```console
pip install drf-yasg
```
2. Next we add the installed package in the **INSTALLED_APPS** in **myproject/settings.py**:
```python
INSTALLED_APPS = [
    # ...
    'drf_yasg',
]
```
In  **myBookapp/urls.py** file, we have defined a few different endpoints that map to our API views. we have three additional endpoints that are used for API documentation:
```python 
from django.urls import path
from .views import BookList, BookDetail
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Book API",
        default_version='v1',
        description="API for managing books",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@bookapi.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[],
)

urlpatterns = [
    path('books/', BookList.as_view()),
    path('books/<int:pk>/', BookDetail.as_view()),
    path('openapi/',schema_view.without_ui(cache_timeout=0)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```
- **/openapi/:** This endpoint returns the OpenAPI schema in JSON format, without any UI. This is useful for machine-readable documentation, and can be used by code generation tools to create client libraries or other integrations with the API.

- **/swagger/:** This endpoint displays the API documentation using the Swagger UI. This is a popular user-friendly interface for exploring APIs and interacting with them.

- **/redoc/:** This endpoint displays the API documentation using ReDoc, which is another popular UI for exploring APIs. It provides a clean, minimalist interface that is easy to read and navigate.

All three of these endpoints are powered by the **get_schema_view()** function from drf_yasg, which creates a schema view for the API using the provided openapi.Info object. This object contains metadata about the API such as its title, description, version, and license information.\

Finally, note that we have specified **cache_timeout=0** for all of the schema views. This disables caching of the schema data, which can be useful during development when the API schema may be changing frequently. However, in production it is generally recommended to enable caching to improve performance.\

In **myBookapp/views.py** we add the **swagger_auto_schema** decorator is used to provide metadata about the API endpoints for use in generating the **OpenAPI** schema and **Swagger UI** documentation.

```python
from django.shortcuts import render

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from drf_yasg.utils import swagger_auto_schema

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @swagger_auto_schema(operation_description="Retrieve the list of books")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new book")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @swagger_auto_schema(operation_description="Retrieve a book by ID")
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a book by ID")
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a book by ID")
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

For example, in the **BookList** view, the get method is decorated with **swagger_auto_schema** and given an **operation_description** parameter. This parameter provides a brief description of what the operation does, and is used to generate the "Operation Summary" section of the Swagger UI documentation for that endpoint.

Similarly, the **BookList** view's post method is decorated with **swagger_auto_schema** and given its own operation_description parameter, which provides a description of what the operation does.

The **BookDetail** view's get, put, and delete methods are similarly decorated with **swagger_auto_schema** and given their own **operation_description** parameters.

By adding these **swagger_auto_schema** decorators, we are able to provide more detailed and accurate metadata about our API endpoints, which in turn can improve the generated documentation and make it easier for users to understand and use our API. \

In conclusion, Swagger and OpenAPI are powerful tools for documenting and testing APIs. They allow developers to easily create comprehensive and interactive documentation for their APIs, making it easier for users to understand and utilize the available endpoints. The use of Swagger and OpenAPI can also help to reduce development time and errors by enabling automatic code generation and standardizing API specifications. Additionally, the integration of Redoc and other tools like drf-yasg can enhance the documentation and user experience even further. Overall, Swagger and OpenAPI are essential components of modern API development and can greatly improve the accessibility, usability, and functionality of APIs.