# **5.02 Consume Rest APIs**

## **Overview**
Previously we saw how to create a GET request using :
- **Postman**
- **curl**
- **Requests** 
- **Aiohttp**

This section is aimed teach the learners how to work with JSON responses in HTTP and show you how to write simple Python scripts to create your own HTTP clients.

**Keywords**:(JSON, HTTP requests, responses, status codes, headers, methods, Python Requests library, parsing, HTTP clients.)
## **Handle HTTP JSON responses**

- **JSON** : stands for JavaScript Object Notation, and it is a lightweight data interchange format. It is used to transmit data between a server and a web application as an alternative to XML. JSON is easy to read and write, and it is also easy to parse and generate data using various programming languages. In JSON, data is represented as a collection of key-value pairs, where the keys are strings and the values can be any valid JSON data type, such as numbers, strings, booleans, arrays, or objects. JSON is commonly used in web APIs and web services to transmit data between different systems.
- **HTTP responses**: HTTP responses are messages sent by a server to a client in response to an HTTP request. An HTTP response typically consists of a status line, headers, and a message body.

    1. The status line contains a status code, which indicates the status of the requested resource, such as whether the request was successful or not.

    2. The headers provide additional information about the response, such as the content type, content length, and caching directives.

    3. The message body contains the actual data returned by the server, which can be in different formats such as HTML, XML, or JSON.

HTTP responses can also include cookies, which are small pieces of data that a server sends to a client and are stored on the client's computer. Cookies can be used to maintain a session, track user behavior, and personalize user experiences.
- **JSON parsing** refers to the process of converting a JSON response string into a usable data structure in your code.

 Here are some steps on how to handle HTTP JSON responses:

1. Send an HTTP request to the server using a Python library such as `requests`.
2. Get the response from the server, which will include the HTTP status code, headers, and message body.
3. Check the HTTP status code to see if the request was successful or not. A status code in the range of 200-299 indicates success, while codes in the range of 400-499 indicate client-side errors and codes in the range of 500-599 indicate server-side errors.
4. Parse the message body of the response as JSON data using a JSON parsing library, such as `json`.
5. Access the data in the JSON object to extract the relevant information and use it in your program.

Here's an example of Python code that demonstrates how to handle a JSON response from an HTTP request:

```python
import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    print("Title:", data["title"])
    print("Body:", data["body"])
else:
    print("Error:", response.status_code)
```

In this example, we send an HTTP GET request to the URL "https://jsonplaceholder.typicode.com/posts/1". If the request is successful, we parse the response as JSON using `json.loads()`, and we print the title and body of the post. If the request fails, we print the HTTP status code returned by the server.


## **Creating http client**
- HTTP client is a software application or program that sends HTTP requests to a web server and receives HTTP responses in return. HTTP clients can be used to interact with web services and web APIs, and they are essential components of many web applications.

- HTTP clients can be built using a variety of programming languages and frameworks, and there are many libraries available to simplify the process of making HTTP requests and handling HTTP responses. Some popular HTTP client libraries for Python include the Requests library, the httplib library, and the urllib library.

- HTTP clients can send different types of HTTP requests, such as GET, POST, PUT, DELETE, and more. They can also send and receive various types of data, including text, HTML, JSON, and binary data.
- When we talk about creating our own HTTP client, we mean that we are creating a software application or program that can send HTTP requests to a web server and receive HTTP responses in return, using our own custom code or library.

- This can be useful in a variety of scenarios, such as when we need to interact with a web service or API that doesn't have an existing client library, or when we want more fine-grained control over the way our HTTP requests are constructed and sent.

- Creating our own HTTP client typically involves using a programming language like Python and a library or module that provides functionality for making HTTP requests, such as the Requests library. With these tools, we can write code that constructs HTTP requests with custom headers, query parameters, and request bodies, sends them to a web server, and handles the responses that we receive.

- By creating our own HTTP client, we can tailor our requests and responses to the specific needs of our application, and gain a deeper understanding of how HTTP works under the hood.

Here are the basic steps to create your own HTTP client using Python:

1. Import the `requests` library: `import requests`

2. Construct an HTTP request using the `requests` library: `response = requests.get(url, headers=headers, params=params)`

   In this example, `url` is the URL of the resource you want to request, `headers` is a dictionary of any additional HTTP headers you want to include in the request, and `params` is a dictionary of any query parameters you want to include in the request.

3. Handle the HTTP response: 

   You can access the response status code using `response.status_code` and the response content using `response.content` or `response.text`.

4. Optionally, you can use the `requests.Session()` object to create a persistent session that can be used to send multiple requests to the same web server.

   For example, you can create a session object like this: `session = requests.Session()` and use it to send requests like this: `response = session.get(url, headers=headers, params=params)`

   Using a session can be more efficient than creating a new connection for each request, especially if you're making multiple requests to the same server.

That's the basic idea! Of course, there are many other features and options available in the `requests` library that you can use to customize your HTTP requests and responses, but these steps should get you started.
The `requests` library provides many other features and options that you can use to customize your HTTP requests and responses. Here are a few examples:



- Request headers: You can add custom headers to your requests using the `headers` parameter. For example, you might need to include an `Authorization` header with an access token to authenticate your request.

- Request parameters: You can include query parameters or form data in your requests using the `params` or `data` parameters, respectively.

- Request timeout: You can set a timeout for your requests using the `timeout` parameter. This can be useful if you don't want your program to hang indefinitely if the server doesn't respond.

- Session parameters: When using a `requests.Session()` object, you can set session-level parameters like default headers or timeout values that will be used for all requests sent using that session.

- Response content: You can access the response content in different formats, such as raw bytes (`response.content`), a decoded string (`response.text`), or a JSON object (`response.json()`).

- Response status: In addition to the response status code (`response.status_code`), you can also check if the request was successful using the `response.ok` attribute, which returns `True` if the status code is in the `2xx` range.

These are just a few examples of the many features and options available in the `requests` library. For more information, I recommend checking out the official documentation: https://docs.python-requests.org/en/latest/

The main difference between using `requests` and `requests.Session()` is that `requests` creates a new HTTP session for every request, while `requests.Session()` allows you to reuse the same session for multiple requests. 

- When you use `requests` to send a request to a web server, it creates a new HTTP session for that request. This means that any cookies or authentication tokens that were set during a previous request will not be automatically included in the new request. Additionally, if you're making multiple requests to the same web server, each request will have to establish a new TCP connection, which can be less efficient.

- On the other hand, when you use `requests.Session()`, you create a session object that can be used to send multiple requests to the same web server. This allows you to reuse any cookies or authentication tokens that were set during a previous request, as well as maintain a persistent TCP connection to the server, which can improve performance.

- Using `requests.Session()` is particularly useful when you need to make multiple requests to the same web server, such as when you're working with a web API or a web application that requires authentication. By using the same session object for all requests, you can simplify your code and avoid having to repeat the same setup code for each request.

## **Conceptualize database REST operations**

To conceptualize database REST operations means to understand how REST (Representational State Transfer) principles can be applied to database operations in order to create a web-based API for interacting with the database. 

In other words, RESTful database operations provide a way to interact with a database through a web API using HTTP methods (GET, POST, PUT, DELETE), URLs, and response formats like JSON or XML. This allows developers to access and manipulate data in the database using simple and standardized HTTP requests, instead of relying on proprietary database-specific protocols.

To conceptualize database REST operations, you'll need to understand how to design a RESTful API that maps database resources to URLs and HTTP methods. You'll also need to consider how to handle authentication, authorization, and error handling for the API. 

Some key concepts to keep in mind when designing a RESTful API for a database include:

- Resources: These are the data objects in the database that the API will expose. Resources should be mapped to URLs and accessed using HTTP methods.

- Representations: These are the formats used to represent the resources in the API responses, such as JSON or XML.

- HTTP methods: These are the standard HTTP methods used to perform CRUD (Create, Read, Update, Delete) operations on resources in the database.

- URLs: These are the endpoints that map to specific resources in the API. URLs should be designed to be human-readable and intuitive.

- Authentication: This is the process of verifying the identity of the user making the API request. Common authentication mechanisms include OAuth, JWT, and basic authentication.

- Authorization: This is the process of determining whether the authenticated user has permission to access or manipulate the requested resource.

- Error handling: This involves providing informative error messages and status codes to the user in case of errors or invalid requests.

In order to create a RESTful API for a database, you'll need to use a programming language and a framework that supports HTTP requests and responses. Some popular options include Flask, Django, and Express.js.

Here's a table that shows a comparison between REST verbs and their equivalent operations in SQL, along with some example code:

| REST Verb | SQL Operation | Example |
| --------- | ------------- | ------- |
| GET       | SELECT        | `SELECT * FROM employees` |
| POST      | INSERT        | `INSERT INTO employees (name, salary) VALUES ('John Doe', 50000)` |
| PUT/PATCH | UPDATE        | `UPDATE employees SET salary=60000 WHERE id=123` |
| DELETE    | DELETE        | `DELETE FROM employees WHERE id=123` |




