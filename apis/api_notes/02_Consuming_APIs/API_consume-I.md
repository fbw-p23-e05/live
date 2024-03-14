# **5.02 Consume REST APIs**
## **Overview** 
API consumption is the goal of publishing APIs. It's a key phase in the API lifecycle. The whole reason APIs are created is so that someone consume APIs in order to connect applications and services./
The goal of this submodule is to introduce learner to different ways to consume REST APIs using Postman, curl, and in Python using the Requests (synchronous) + Aiohttp (Asynchronous) packages.
## **Objective**
Objectives
By the end of this submodule, the learners should be able to:

1. Create GET requests using Postman, curl, Requests, and Aiohttp 
2. Handle HTTP JSON responses
3. Write basic scripts to create own HTTP clients in Python
4. Conceptualize database REST operations
**Keywords** :(REST, API, API key, HTTP methods, Headers, Query parameters, Request payload, Response, JSON, XML, Authentication, cURL, Postman, Requests library, Aiohttp library, Asynchronous programming, Concurrency, Error handling, Rate limiting, Pagination.)
## **APIs & API KEY**
- An API, or Application Programming Interface, is a set of rules and protocols that specifies how software components should interact with each other. It's a way for different software systems to communicate with each other and exchange data, without needing to know the details of how each system works. APIs are often used to build applications that integrate with third-party services, like social media platforms, payment gateways, and more.

- An API key is a unique identifier that is used to authenticate and authorize access to an API. Think of it like a password or a security token that grants permission to use the API. When you sign up for an API, you will typically be given an API key that you need to include in your requests to the API. This key allows the API provider to track usage and enforce access limits, as well as provide customized responses based on your specific account and usage. In short, an API key is a way to ensure secure and controlled access to an API.

- In this link we find a list of free APIs where some of them require and API KEY and others don't :
https://github.com/public-apis/public-apis 
## Consuming REST APIs
- When we talk about consuming REST APIs, we mean using them to access data and functionality provided by another application or service. The term "consume" is used because we are essentially using the API like a product or service, taking advantage of its features and capabilities.

- Consuming REST APIs is important because it allows us to leverage the functionality of other systems in our own applications. Instead of building everything from scratch, we can use APIs to quickly and easily access data and functionality that we need. For example, if we're building an e-commerce application, we might use an API provided by a payment gateway to handle credit card transactions. Or if we're building a weather app, we might use an API provided by a weather service to get up-to-date weather data for a particular location.

- REST APIs are especially popular because they are based on a set of simple, lightweight standards, such as HTTP, JSON, and XML, that are widely supported by different programming languages and platforms. This makes it easy to consume REST APIs from a variety of different environments, including web applications, mobile apps, and desktop applications.
### **Consuming REST APIs using Postman**
- **Postman** is a popular API testing tool that allows developers to test and interact with APIs using a graphical user interface. It supports a wide range of API formats, including REST, SOAP, and GraphQL, and makes it easy to send requests, view responses, and test different scenarios.
#### **Without an API KEY**
Here's how to create a GET request using Postman for an API without an API key:

1. Open Postman and create a new request by clicking the "New" button in the top-left corner.
2. In the new request window, select "GET" as the HTTP method.
3. Enter the URL of the API you want to call in the "Enter request URL" field.
4. Click the "Send" button to send the request to the API.
5. View the response in the "Body" tab of the response pane.
#### **With an API KEY**
And here's how to create a GET request using Postman for an API with an API key:

1. Open Postman and create a new request by clicking the "New" button in the top-left corner.
2. In the new request window, select "GET" as the HTTP method.
3. Enter the URL of the API you want to call in the "Enter request URL" field.
4. Click on the "Headers" tab and add a new header called "X-API-Key".
5. Enter your API key as the value for the "X-API-Key" header.
6. Click the "Send" button to send the request to the API.
7. View the response in the "Body" tab of the response pane.

In both cases, you can use the Postman interface to view and modify the request parameters, headers, and body as needed, making it easy to test and debug your API calls.

### **Consuming REST APIs using cURL**
- **cURL** is a command-line tool for transferring data using various protocols, including HTTP, FTP, and SMTP. It's widely used by developers and system administrators to test and interact with APIs, as well as to automate tasks that involve sending and receiving data over the internet.

#### **Without an API KEY**
Here's how to create a GET request using cURL for an API without an API key:

1. Open a command prompt or terminal window.
2. Type the following command and replace the URL with the URL of the API you want to call:
```console 
curl <URL>
```
3. Press Enter to send the request to the API.
4. View the response in the terminal window.

#### **With an API KEY**
And here's how to create a GET request using cURL for an API with an API key:

1. Open a command prompt or terminal window.
2. Type the following command and replace the URL with the URL of the API you want to call:
```console
curl -H "X-API-Key: <API_KEY>" <URL>
```
3. Replace <API_KEY> with your API key.
4. Press Enter to send the request to the API.
5. View the response in the terminal window.

In both cases, you can use cURL to add additional options and parameters to your request, such as setting custom headers, specifying a user agent, or sending data in the request body. The cURL documentation provides more information on the various options and parameters that are available.
### **Consuming REST APIs using Requests**
**Requests** is a popular Python library for making HTTP requests. It simplifies the process of sending requests and handling responses, and supports a wide range of HTTP methods and authentication mechanisms.
#### **Without an API KEY**
Here's how to create a GET request using Requests for an API without an API key:

1. Open a Python interpreter or create a new Python file.
2. install requests library using **pip**
```console
pip install requests
```
3. Import the Requests library by adding the following line at the beginning of your code:
```python
import requests
```
4. Send a GET request to the API by calling the **requests.get()** function and passing the URL of the API as an argument:
```python
response = requests.get('<URL>')
```
5. View the response by accessing the **content** attribute of the **response** object:
```python
print(response.content)
```
#### **With an API KEY**
Here's how to create a GET request using Requests for an API without an API key:

1. Open a Python interpreter or create a new Python file.
2. install requests library using **pip**
```console
pip install requests
```
3. Import the Requests library by adding the following line at the beginning of your code:
```python
import requests
```
4. Send a GET request to the API by calling the requests.get() function and passing the URL of the API as an argument, along with a dictionary containing the API key as a header:
```python
headers = {'X-API-Key': '<API_KEY>'}
response = requests.get('<URL>', headers=headers)

```
5. Replace <API_KEY> with your API key.
6. View the response by accessing the **content** attribute of the **response** object:
```python
print(response.json)
```
In both cases, you can use the Requests library to add additional options and parameters to your request, such as setting custom headers, specifying query parameters, or sending data in the request body. The Requests documentation provides more information on the various options and parameters that are available.
### **Consuming REST APIs using Aiohttp**
Aiohttp is a Python library for making HTTP requests asynchronously. It's built on top of Python's asyncio framework, which enables efficient and scalable asynchronous I/O operations. Aiohttp is particularly useful for applications that need to make multiple requests in parallel, such as web scrapers, chatbots, and IoT devices.

#### **With an API KEY**
Here's how to create a GET request using Aiohttp for an API without an API key:

1. Open a Python interpreter or create a new Python file.
2. Import the Aiohttp library by adding the following line at the beginning of your code:
```python 
import aiohttp
```
3. Send a GET request to the API by creating a new aiohttp.ClientSession() object, calling the session.get() method, and passing the URL of the API as an argument:
```python 
async with aiohttp.ClientSession() as session:
    async with session.get('<URL>') as response:
        print(await response.json())
```
4. View the response by accessing the text() method of the response object.
#### **With an API KEY**
1. Open a Python interpreter or create a new Python file.
2. Import the Aiohttp library by adding the following line at the beginning of your code:
```python 
import aiohttp
```
3. Send a GET request to the API by creating a new aiohttp.ClientSession() object, calling the session.get() method, and passing the URL of the API as an argument:
```python 
headers = {'X-API-Key': '<API_KEY>'}
async with aiohttp.ClientSession() as session:
    async with session.get('<URL>', headers=headers) as response:
        print(await response.json())

```
4. Replace <API_KEY> with your API key.
5. View the response by accessing the text() method of the response object.

In Python, `async` and `await` are keywords that are used to define and work with asynchronous code. Asynchronous code allows you to run multiple tasks concurrently, without blocking the execution of other tasks.

Here's a brief explanation of what `async` and `await` do:

- `async`: This keyword is used to define a coroutine function, which is a function that can be paused and resumed during its execution, allowing other tasks to be run in the meantime.

- `await`: This keyword is used inside a coroutine function to pause its execution and wait for the completion of another coroutine function or an asynchronous operation, such as an HTTP request or a database query.

- In the context of making HTTP requests with libraries like Aiohttp, `async` and `await` allow you to send multiple requests concurrently without blocking the execution of other parts of your code. This can significantly improve the performance of your application, especially when dealing with large amounts of data.

- In the example code I provided earlier, the `async with` statement is used to create an asynchronous context manager that handles the creation and cleanup of an `aiohttp.ClientSession()` object. The `async with session.get()` statement then sends a GET request to the specified URL, and the `await response.text()` statement waits for the response to be received and returns the response body as text.

- Overall, `async` and `await` are powerful features of Python that enable efficient and scalable asynchronous programming, and they're particularly useful for applications that need to make multiple HTTP requests or perform other I/O operations concurrently.
## Querying REST APIs
To get a group of elements and sort them when consuming a REST API, you can use query parameters. Query parameters allow you to customize the response that you receive from the API by specifying certain criteria. Here are a few examples of how you can use query parameters to get a group of elements and sort them:

1. Filtering by a specific attribute:
To get a group of elements that share a specific attribute value, you can use a filter query parameter. For example, if you are consuming a REST API that returns a list of products, you can use a filter query parameter to get only the products that are in a specific category:
```
https://api.example.com/products?category=electronics
```
This will return a list of products that have the category "electronics".

2. Sorting by a specific attribute:
To sort the elements returned by a REST API by a specific attribute, you can use a sort query parameter. For example, if you are consuming a REST API that returns a list of products, you can use a sort query parameter to sort the products by price:
```
https://api.example.com/products?sort=price
```
This will return a list of products sorted by price.

3. Pagination:
To get a specific subset of the elements returned by a REST API, you can use pagination. Pagination is typically used when the response contains a large number of elements. The API will return a subset of the elements in each response, and you can use query parameters to specify which subset you want to receive. For example, if you are consuming a REST API that returns a list of products, you can use the page and limit query parameters to get a specific page of products:
```
https://api.example.com/products?page=2&limit=10
```
This will return the second page of products, with a maximum of 10 products per page.
In addition to filtering, sorting, and pagination, there are many other types of queries that you can use when consuming REST APIs. Here are a few examples:

4. Searching:
You can use a search query parameter to search for elements that match a specific keyword or phrase. For example, if you are consuming a REST API that returns a list of books, you can use a search query parameter to find books that have "Python" in the title:
```
https://api.example.com/books?search=python
```
This will return a list of books that have "Python" in the title.

5. Aggregating:
You can use an aggregation query parameter to group the elements returned by a REST API by a specific attribute and return aggregated information, such as counts, averages, or sums. For example, if you are consuming a REST API that returns a list of sales transactions, you can use an aggregation query parameter to group the transactions by month and return the total sales for each month:
```
https://api.example.com/sales?aggregate=month&sum=amount
```
This will return the total sales amount for each month.

6. Filtering by range:
You can use a range query parameter to filter the elements returned by a REST API based on a range of values. For example, if you are consuming a REST API that returns a list of products, you can use a range query parameter to get only the products that are within a specific price range:
```
https://api.example.com/products?price_range=10-50
```
This will return a list of products that have a price between 10 and 50.

7. Combining queries:
You can combine multiple query parameters to create complex queries that filter, sort, and paginate the elements returned by a REST API. For example, you can use a combination of filtering, sorting, and pagination to get a specific group of products that are sorted by price and displayed on a specific page:
```
https://api.example.com/products?category=electronics&sort=price&page=2&limit=10
```
This will return the second page of electronics products sorted by price, with a maximum of 10 products per page.

By using a combination of these query parameters, you can create powerful queries that enable you to get the specific group of elements that you need when consuming a REST API.\
Moreover when we are using **requests** or **aiohttp** we can add these params to our get request as follow:
```python
params={'param1':param1,'param2':param2,'param3':param3}
response = requests.get('<URL>', params=params)
```
this is similar to 
```
https://api.example.com/products?param1=param1&param2=param2&param3=param3
```


