# **5.03 Create REST api**
## **Overview**
Testing in Django REST Framework (DRF) APIs is an important aspect of ensuring that your application is functioning correctly and that it meets the required specifications. Testing helps in identifying and fixing issues before they reach production, which can save a lot of time and resources in the long run. In this submodule you will learn how to perform tests on different DRF parts.\
**keywords**: \
(Test Client, Unit Tests, Integration Tests, Functional Tests, Test Fixtures, Test Coverage, Load Testing, Assertion, Mocking, TDD, Serializer, Test Runner, Django Test Framework, Pytest, Postman, Insomnia, Performance Testing, Regression Testing, Security Testing, Black Box Testing, White Box Testing, Test Suite, Test Case, Test Result, Test Environment, CI, CD, DevOps, Acceptance Testing, UAT.)

## Testing in Django Rest Framework
- **Test Client:** The DRF Test Client is a Python module that provides a simple way to test views in the Django framework. The test client allows you to simulate a user interacting with the application, sending requests to the views, and receiving responses.

- **Unit Tests:** Unit tests are used to test individual parts of an application in isolation. In the case of DRF APIs, unit tests are used to test the individual endpoints or views.

- **Integration Tests:** Integration tests are used to test the interaction between different components of an application. In the case of DRF APIs, integration tests are used to test the integration of different views or endpoints with the database, other APIs, or third-party services.

- **Functional Tests:** Functional tests are used to test the application as a whole, simulating how a user interacts with the application. In the case of DRF APIs, functional tests are used to test the complete functionality of the API, from the request to the response.

- **Test Fixtures:** Test fixtures are a set of pre-defined data or configuration that is loaded before each test. In the case of DRF APIs, test fixtures can be used to set up test data in the database or create test users.

- **Test Coverage:** Test coverage refers to the percentage of code that is covered by tests. Test coverage is an important metric in testing as it helps ensure that all code paths are tested.

- **Load Testing:** Load testing is the process of testing the performance of an application under various load conditions. In the case of DRF APIs, load testing can be used to test the performance of the API under high traffic conditions.

- **Assertion:** An assertion is a statement that checks whether a certain condition is true or false. In the case of DRF API testing, assertions can be used to check whether the response status code, response content, and other properties are correct.

- **Mocking:** Mocking is a technique used in testing to create a fake version of an object or function. In the case of DRF API testing, mocking can be used to create fake responses from external APIs or services.

- **Test Driven Development (TDD):** Test-driven development is a software development process that emphasizes writing tests before writing code. In the case of DRF API development, TDD can be used to ensure that the API meets the required specifications and functions correctly.

## Working example
- A true feeling of satisfaction comes when you get all the test running. In our Book application we will run the following test.
1. we import the following classes :
```python 
from rest_framework.test import APIClient, APITestCase
```


- **APIClient** is a class provided by the **rest_framework.test** module which is used to simulate **HTTP** requests to an API and receive **HTTP** responses. It provides methods to perform common **HTTP** requests like GET, POST, PUT, DELETE, etc.
- **APITestCase** is a class provided by the **rest_framework.test** module that extends Django's built-in TestCase class and provides additional functionalities to write tests for API endpoints. It sets up the test database and provides methods to make requests using the **APIClient** class and to check the responses.
2. Afterwards we import the following module
```python
from rest_framework import status
```
- **status** is a module provided by the **Django REST framework** that defines standard **HTTP** response status codes used by RESTful APIs. It provides constants for all the common HTTP status codes like 200 OK, 404 Not Found, 500 Internal Server Error, etc.
3. Next we import the rest packages 
```python
from django.urls import reverse
from datetime import date, timedelta
from django.utils.text import slugify
from .models import Book
from .serializers import BookSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
```
4. When testing we need to create a class that extends from **APITestCase**.
```python
class BookTests(APITestCase):
```
**BookTests** is a class that extends the **APITestCase** class provided by the Django REST framework. This class defines test cases for testing the **API** endpoints related to books.

By inheriting from the **APITestCase** class, this test case class has access to various methods provided by the APITestCase class, such as **setUp()**, **tearDown()**, and **client**.

The **setUp()** method is called before every test case, and it is used to set up the test environment, such as creating test data or setting up the APIClient.
```python
def setUp(self):
        """
        Initialize test data
        """
        self.client = APIClient()
        self.admin_user = User.objects.create_user(
            "admin", "admin@test.com", "testpassword", is_staff=True
        )
        self.token = Token.objects.create(user=self.admin_user)
        self.user = User.objects.create_user("user", "admin@test.com", "testpassword")
        self.user_token = Token.objects.create(user=self.user)
        self.book = Book.objects.create(
            title="The Alchemist",
            author="Paulo Coelho",
            description="A book about following your dreams",
            published_date=date.today() - timedelta(days=7),
            is_published=False,
        )
        self.valid_payload = {
            "title": "The Alchemist 1",
            "author": "Paulo Coelho",
            "description": "A book about following your dreams",
            "published_date": date.today() - timedelta(days=7),
            "is_published": False,
        }
        self.invalid_payload = {
            "title": "",
            "author": "",
            "description": "",
            "published_date": date.today() + timedelta(days=7),
            "is_published": False,
        }
```

- **self.client = APIClient()** creates an instance of the APIClient class, which can be used to make HTTP requests to the API.

- **self.admin_user = User.objects.create_user()** creates an admin user in the test database, which can be used to test admin-only endpoints.

- **self.token = Token.objects.create()** creates an authentication token for the admin user, which can be used to authenticate requests to admin-only endpoints.

- **self.user = User.objects.create_user()** creates a regular user in the test database, which can be used to test user-only endpoints.

- **self.user_token = Token.objects.create()** creates an authentication token for the regular user, which can be used to authenticate requests to user-only endpoints.

- **self.book = Book.objects.create()** creates a book instance in the test database, which can be used to test endpoints that interact with the Book model.

- **self.valid_payload** is a dictionary containing valid data for creating or updating a book instance.

- **self.invalid_payload** is a dictionary containing invalid data for creating or updating a book instance.

The **tearDown()** method is called after every test case, and it is used to clean up the test environment, such as deleting test data or closing the **APIClient**.

The **client** attribute is an instance of the **APIClient** class, which is used to simulate HTTP requests and receive HTTP responses in the tests.
5. After setting the data, we perform the tests we want.
- **Test to get all books**
```python
def test_get_all_books(self):
        response = self.client.get(reverse("book_list"))
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
```
 This test method tests the functionality of the GET method for the Book model's API view. It sends a GET request to the /books/ endpoint, retrieves all Book instances from the test database, serializes them into a list of dictionaries, and compares the serialized data with the data returned in the response to ensure that they match. Finally, it checks that the response status code is HTTP 200 OK, indicating that the request was successful. This ensures that the GET method for the Book API view is working as expected and returns the correct data in the correct format.
- **Test to get a single book**
```python
def test_get_single_book(self):

        response = self.client.get(reverse("book_detail", args=[self.book.id]))
        book = Book.objects.get(id=self.book.id)
        serializer = BookSerializer(book)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
```
This test method tests whether the **book_detail** endpoint of the Django REST Framework API works correctly. Specifically, it checks that the endpoint retrieves a single Book instance with the correct serialized data when given the ID of the Book instance.\

To accomplish this, the test method sends a GET request to the **book_detail** endpoint with the ID of a Book instance, retrieves the Book instance with the same ID from the test database, serializes the Book instance into a dictionary using the BookSerializer class, and then compares the data in the response to the serialized data for the Book instance.\

If the serialized data in the response matches the expected serialized data for the Book instance, and the response status code is HTTP 200 OK (indicating success), then the test method passes. Otherwise, the test method fails, indicating a problem with the **book_detail** endpoint.
-  **Test to create a valid book as an admin**
```python
def test_create_valid_book(self):

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        response = self.client.post(
            reverse("book_list"), data=self.valid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
```
This test method tests whether the `book_list` endpoint of the Django REST Framework API works correctly for creating a valid `Book` instance. Specifically, it checks that the endpoint returns a response with an HTTP status code of 201 CREATED when given valid input data.

Here's a brief explanation of what each line does:

- `self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)` sets the authorization header for the test client to include a token for an admin user. This is necessary because the `book_list` endpoint is protected and requires authentication.

- `response = self.client.post(reverse("book_list"), data=self.valid_payload, format="json")` sends a POST request to the `/books/` endpoint, where the data in the request body is the `valid_payload` dictionary serialized as JSON. The `book_list` view function is called, which creates a new `Book` instance with the data in the request body, and returns the serialized data for the new instance in the response. The response is stored in the `response` variable.

- `self.assertEqual(response.status_code, status.HTTP_201_CREATED)` checks that the response status code is equal to the HTTP 201 CREATED status code, indicating that the request was successful and a new `Book` instance was created.

If the response status code is HTTP 201 CREATED (indicating success), then the test method passes. Otherwise, the test method fails, indicating a problem with the `book_list` endpoint for creating a valid `Book` instance.


- **Test to create a valid book as a user**
```python
def test_create_book_as_user(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_token.key)
        url = reverse("book_list")
        data = {
            "title": "New Book",
            "author": "New Author",
            "description": "New Description",
            "published_date": "2021-01-01",
            "is_published": True,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
```
This test method tests whether the `book_list` endpoint of the Django REST Framework API works correctly for preventing users from creating a new `Book` instance. Specifically, it checks that the endpoint returns a response with an HTTP status code of 403 FORBIDDEN when given input data from a non-admin user.

Here's a brief explanation of what each line does:

- `self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_token.key)` sets the authorization header for the test client to include a token for a non-admin user. This is necessary because the `book_list` endpoint is protected and requires authentication.

- `url = reverse("book_list")` retrieves the URL for the `book_list` endpoint.

- `data = {...}` defines a dictionary that represents the input data for the POST request, which includes a new `Book` instance's attributes.

- `response = self.client.post(url, data)` sends a POST request to the `book_list` endpoint, where the data in the request body is the `data` dictionary. The `book_list` view function is called, which tries to create a new `Book` instance with the data in the request body, but the request fails due to insufficient permissions. The response is stored in the `response` variable.

- `self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)` checks that the response status code is equal to the HTTP 403 FORBIDDEN status code, indicating that the request was not authorized due to insufficient permissions.

If the response status code is HTTP 403 FORBIDDEN (indicating success), then the test method passes. Otherwise, the test method fails, indicating a problem with the `book_list` endpoint's authentication or permission settings for creating a new `Book` instance.
- **Test create book without authorization**
```python
def test_authentication_required_for_book_list(self):
        url = reverse("book_list")
        response = self.client.post(url, data=self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
```
This is a test method to check that authentication is required to access the book list. The test sends a POST request to the URL associated with the book_list view and provides a valid payload as data. Since authentication is required for this endpoint, the expected response status code is 401 UNAUTHORIZED. The test asserts that the response status code matches the expected status code.
- **Test to create an invalid book**
```python 
def test_create_invalid_book(self):
       
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        response = self.client.post(
            reverse("book_list"), data=self.invalid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
```
This is a test method that tests the behavior of the book_list view when an invalid book payload is provided during a POST request. The method first sets the authorization credentials of the client using an authentication token. It then sends a POST request to the book_list view, providing an invalid payload as data. The test expects the view to return a 400 BAD REQUEST status code, indicating that the payload is not valid. Finally, the method asserts that the response status code matches the expected status code.
- **Test to update a book** 
```python
def test_update_book(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        updated_payload = self.valid_payload.copy()
        updated_payload["title"] = "The Alchemist Revised"
        response = self.client.put(
            reverse("book_detail", args=[self.book.id]),
            data=updated_payload,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            slugify(response.data["title"]), slugify(updated_payload["title"])
        )
```
This is a test case method to test updating an existing book using PUT HTTP method. Here's a breakdown of what the method does:

- The method first sets the credentials for the client using the authentication token of the admin user.

- It then creates an updated version of the valid payload by making a copy of it and changing the title.

- Next, the method sends a PUT request to the endpoint for updating the book with the specified ID (self.book.id) and passes the updated payload as the data in JSON format.

- It then asserts that the response status code is HTTP 200 OK, indicating that the update was successful.

Finally, the method asserts that the title of the updated book in the response data matches the updated title in the payload.
- **Test to delete a book** 
```python 
def test_delete_book(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.delete(reverse("book_detail", args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
```
This is a test case method that tests deleting a book object using the DELETE method. The method first sets the authentication token for an admin user, then sends a DELETE request to the URL endpoint for deleting a single book, passing the ID of the book to be deleted as an argument in the URL.
Finally, the method checks if the response status code is 204 No Content, which indicates that the deletion was successful.
- **Test to handle custom exceptions** 
```python
def test_custom_exception_handler(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.post(
            reverse("book_list"), data=self.invalid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("detail" in response.data)
```
- This is a unit test to test the custom exception handler implemented in the Django project. The test is checking whether the custom exception handler is correctly handling invalid data and returning an appropriate error message.

- The test sends a POST request to the 'book_list' endpoint with invalid data. The custom exception handler should then catch the exception and return a response with a status code of 400 (Bad Request) and an error message in the response data.

- The assertion checks that the response has a status code of 400 and that the response data contains a 'detail' key. If the test passes, it confirms that the custom exception handler is working correctly.
**"Ah, nothing like the sweet, sweet feeling of all tests passing." Unknown**