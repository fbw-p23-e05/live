# **5.03 Create REST api**

## **Overview**
In Django Rest Framework (DRF), data validation and sanitization are important steps in ensuring the integrity and security of the data being passed through the API. This submodule is designed to teach you how to  validate, sanitize RESTful APIs using Django REST Framework (DRF) alongside with exception handeling.
**Keywords** 
(Validation: Serializer, fields, required, default, validators, error_messages, client-side validation, server-side validation, nested data structures, file uploads, custom validation rules, conditional validation rules, ValidationError.\

Sanitization: Serializer, fields, to_internal_value, built-in sanitizers, custom sanitizers, strip_tags, escape_html, binary data, security vulnerabilities, SQL injection, cross-site scripting (XSS) attacks.)
## **Data Validation**

- Data validation is a process of ensuring that the input data provided by the user is correct and meets the specified requirements. It's important because it helps ensure data integrity and prevent errors from occurring.

- DRF provides serializers for data validation. Serializers are classes that define the fields and the validation rules for each field. You can define required fields, default values, and custom validation rules.

- DRF comes with built-in validators for common data types, such as email, URL, and date fields. You can also create custom validators that check for specific requirements.

- When a validation error occurs, DRF raises a `ValidationError` exception. The exception contains a dictionary of error messages for each invalid field.

- You can customize error messages by adding a `message` parameter to your validators or by overriding the `get_error_message()` method in your serializer.

- DRF supports both client-side validation (checking data before it's sent to the server) and server-side validation (checking data on the server after it's received).\


- The validation take place in the model and the serializers. In our book projects we will add two built in validators and two customised validators. \
In **myBookaap/serializerspy** we add the following :
```python 
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Book
from datetime import date
from rest_framework.validators import MaxLengthValidator
class UniqueTitleValidator:
    def __call__(self, value):
        if Book.objects.filter(title=value).exists():
            raise ValidationError("A book with this title already exists.")

class PastDateValidator:
    def __call__(self, value):
        if value > date.today():
            raise ValidationError("Published date must be in the past.")

class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField( required=True, validators=[UniqueTitleValidator(),MaxLengthValidator(200)])
    author = serializers.CharField(required=True,validators=[MaxLengthValidator(200)])
    published_date = serializers.DateField(required=True, validators=[PastDateValidator()])

    class Meta:
        model = Book
        fields = ['id','title','author','description','published_date','is_published']
```
- Here's a brief explanation of the validators :

1. **UniqueTitleValidator:** This validator checks whether a book with the same title already exists in the database. It is implemented as a callable class with a **__call__** method that performs the validation logic. If a book with the same title already exists, it raises a **ValidationError** with an appropriate message.

2. **PastDateValidator:** This validator checks whether the published_date field is in the past. It is also implemented as a callable class with a **__call__** method that performs the validation logic. If the published_date field is not in the past, it raises a **ValidationError** with an appropriate message.
3. **max_length:** This built in validator checks if the maximum length of the title and the author exceeds 200 character or not.
4. **required=True**: a parameter, which means that they must be included in the request data, or else a validation error will be raised
## **Data Sanitization**

- Data sanitization is a process of cleaning up input data to remove any potentially dangerous characters or code that could cause security vulnerabilities, such as SQL injection or cross-site scripting (XSS) attacks.

- DRF provides built-in sanitizers that can be used to clean up input data. For example, the `strip_tags` sanitizer can be used to remove any HTML tags from a string, while the `escape_html` sanitizer can be used to replace any special characters with their HTML entities.

- Sanitization is performed automatically by DRF when data is deserialized. The `to_internal_value` method in a serializer is responsible for cleaning up input data.

- You can also create your own sanitizers to customize the cleaning process. Sanitizers can be added to a serializer's `to_internal_value` method or to a specific field's `run_validation` method.

- Sanitization is an important part of securing your application and protecting against attacks. However, it's important to note that sanitization alone is not enough to ensure security. Other security measures, such as input validation and user authentication, are also necessary to prevent attacks.
- - The sanitization take place in the model and the serializers. In our book projects we will add two built in validators and two customised validators. \
In **myBookaap/serializerspy** we add the following :
```python 
from rest_framework import serializers, validators
from rest_framework.exceptions import ValidationError
from .models import Book
from datetime import date
from django.utils.html import escape, strip_tags
from django.utils.text import slugify

class UniqueTitleValidator:
    def __call__(self, value):
        if Book.objects.filter(title=value).exists():
            raise ValidationError("A book with this title already exists.")

class PastDateValidator:
    def __call__(self, value):
        if value > date.today():
            raise ValidationError("Published date must be in the past.")

class CapitalizeName:
    def __call__(self, value):
        # Capitalize the first letter of each word in the name
        return value.title()

class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200, required=True, validators=[UniqueTitleValidator()],trim_whitespace=True)
    author = serializers.CharField(max_length=200, required=True,trim_whitespace=True)
    published_date = serializers.DateField(required=True, validators=[PastDateValidator()])
    description = serializers.CharField(required=False, allow_blank=True)

    def validate_title(self, value):
        return slugify(strip_tags(value))

    def validate_description(self, value):
        return strip_tags(value)
    
    def validate_author(self,value):
        return strip_tags(value)

    def to_internal_value(self, data):
        # Sanitize is_published field by converting string value to boolean
        if 'is_published' in data:
            data['is_published'] = str(data['is_published']).lower() == 'true'
        return super().to_internal_value(data)

    def to_representation(self, instance):
        # Capitalize the first letter of each word in the author name
        instance.author = CapitalizeName()(instance.author)
        instance.title=CapitalizeName()(instance.title)
        return super().to_representation(instance)

    class Meta:
        model = Book
        fields = ['id','title','author','description','published_date','is_published']

```
- Here is a brief explanation of the sanitizers we added :
1. **validate_title method:** This method applies the `slugify` function to the value of the `title` field. `slugify` is a built-in Django function that takes a string and replaces any spaces, punctuation, or other special characters with hyphens. This ensures that the `title` field only contains alphanumeric characters and hyphens, which can be useful for creating SEO-friendly URLs or for preventing certain types of attacks (such as XSS attacks).

2. **validate_description method:** This method applies the `strip_tags` function to the value of the `description` field. `strip_tags` is a built-in Django function that removes any HTML tags from a string. This is important because it prevents users from inserting HTML or JavaScript code into the `description` field, which could potentially be used to perform XSS attacks.

3. **validate_author method:** This method also applies the `strip_tags` function to the value of the `author` field. This is done to ensure that the `author` field only contains plain text, and to prevent any malicious code or HTML from being injected into the field.

4. **to_internal_value method:** This method is called by Django Rest Framework when the serializer is used to deserialize incoming JSON data. The method checks if the `is_published` field is present in the incoming data, and if it is, converts the value to a boolean and replaces the original value in the data dictionary. This is done to ensure that the `is_published` field is always a boolean value, regardless of whether it is passed in as a string or a boolean.

5. **to_representation method:** This method is called by Django Rest Framework when the serializer is used to serialize a Django model instance into JSON. The method applies the `CapitalizeName` class to the `author` and `title` fields of the instance, which capitalizes the first letter of each word in the field. This is done to ensure that the `author` and `title` fields are always formatted consistently, regardless of how they were originally entered.

6. **CapitalizeName class:** This class is defined at the top of the serializer file and is used to capitalize the first letter of each word in a string. It is used by the `to_representation` method to ensure consistent formatting of the `author` and `title` fields.

7. **trim_whitespace=True** is added to the title and author fields. This means that any whitespace characters (e.g. spaces, tabs, newlines) at the beginning or end of the string will be removed before validation. This ensures that there are no leading or trailing spaces in the title and author fields, which can cause issues when querying or displaying the data.
## Handeling and Creating exeptions:

- Exception handling is the process of dealing with errors or unexpected situations that occur during the execution of a program. In a web application context, exception handling is particularly important because errors that occur during processing can cause the application to crash, return incorrect results, or expose sensitive information to potential attackers.

- In Django Rest Framework (DRF), exception handling is used to catch and respond to errors that occur during the processing of HTTP requests. DRF provides a default exception handling mechanism that returns error responses in a standardized format, but it also allows developers to customize this behavior by defining a custom exception handler function.

- The custom exception handler function can catch and handle any exception that occurs during request processing, and it can return a customized error response. This is useful for handling exceptions that are specific to your application, such as custom validation errors or database errors.

- By handling exceptions properly, you can ensure that your application provides a reliable and secure user experience, even when unexpected errors occur.
We can register this custom exception handler in  **myproject/settings.py** file:
```python
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'myBookapp.views.custom_exception_handler',
}

```
This will override the default DRF exception handler and use your custom handler instead. You can customize the response message and HTTP status code based on your requirements.\
Now in **myBookapp/views.py** file that implements CRUD operations for the Book model, including exception handling using the custom_exception_handler function defined earlier:
```python 
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler
from .permissions import IsAdminOrReadOnly



class **BookList**(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly ,permissions.IsAuthenticatedOrReadOnly,]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        try:
            serializer.save()
        except ValidationError as e:
            raise ValidationError(detail=e.detail)

class **BookDetail**(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_update(self, serializer):
        try:
            serializer.save()
        except ValidationError as e:
            raise ValidationError(detail=e.detail)

    def perform_destroy(self, instance):
        instance.delete()

def custom_exception_handler(exc, context):
    """
    Custom exception handler to handle ValidationError and other exceptions
    """
    if isinstance(exc, ValidationError):
        # Handle ValidationError
        return Response({'detail': exc.detail}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # Handle other exceptions
        response = exception_handler(exc, context)
        if response is not None:
            return response
        else:
            return Response({'detail': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```
- In this example, we define two views: **BookList** for listing and creating new books, and **BookDetail** for retrieving, updating, and deleting books. Both views use the **BookSerializer** to serialize and validate data.

- In **BookList**, we override the perform_create method to catch any ValidationError that occurs during serialization or validation of the data. We raise the error using the raise statement to ensure that the error is propagated up to the exception handler. In **BookDetail**View, we override the perform_update method to catch **ValidationError** in the same way as perform_create.

- Finally, we define the custom_exception_handler function, which is responsible for handling exceptions raised in our views. We check if the exception is a ValidationError and return a response with the error message and a **HTTP_400_BAD_REQUEST** status code. If the exception is not a ValidationError, we defer to the default DRF exception handler, or return a generic error message if the default handler does not produce a response. This function is registered in the **myproject/settings.py** file, as shown in the previous example.