# Today - 2024-02-28

* History of REST API and it's popularity, pros, and cons

* Structure of a Rest API and the role of HTTP

* Concept of Rest Routes and Endpoints

* Demo Project

* Self study

## History and Popularity of REST API

### History:

* REST (Representational State Transfer) was introduced by Roy Fielding in his doctoral dissertation in 2000.

* RESTful APIs gained popularity due to their simplicity, flexibility, and alignment with the principles of the web.

### Pros of REST API:

* Simplicity: REST APIs are simple to understand and use, leveraging HTTP methods for CRUD operations.

* Scalability: RESTful architectures are inherently scalable, as they are stateless and can handle large numbers of clients.

* Flexibility: REST allows for multiple data formats (e.g., JSON, XML) and supports various client devices and platforms.

* Interoperability: RESTful APIs can be easily integrated with other systems, regardless of the programming language or technology stack used.

* Caching: HTTP caching mechanisms can be leveraged to improve performance and reduce server load.

* Statelessness: Each request from a client to the server must contain all the necessary information to understand and process the request.

### Cons of REST API:

* Overfetching/Underfetching: Clients may receive more or less data than they need, leading to inefficient use of network resources.

* Complexity in Large APIs: As APIs grow in complexity, maintaining a consistent and intuitive RESTful interface can become challenging.

* Lack of Standardization: While REST provides principles, there is often variation in how APIs are implemented, leading to potential interoperability issues.

* Limited Support for Real-time Updates: REST is based on stateless communication, making it less suitable for real-time applications that require constant updates.

## Structure of a REST API and the Role of HTTP

### Structure of REST API:

* Resources: Represent entities (e.g., users, products) that can be accessed and manipulated through the API.

* Endpoints: URLs that represent resources and define the operations that can be performed on them.

* HTTP Methods: Actions that can be performed on resources (GET, POST, PUT, DELETE).

* Headers: Additional information sent with requests and responses, such as authentication tokens or content types.

* Status Codes: Indicate the outcome of a request (e.g., 200 for success, 404 for not found).

## Role of HTTP:

* HTTP is the protocol used for communication between clients and servers in a RESTful architecture.

* It provides a standardized way for clients to make requests and servers to respond to them.

* HTTP methods (GET, POST, PUT, DELETE) are used to perform CRUD operations on resources.

* HTTP headers provide metadata about the request or response, such as content type or authentication information.

* HTTP status codes indicate the success or failure of a request and provide additional context about the response.

## Concept of REST Routes and Endpoints

### REST Routes:

* REST routes define the paths (URLs) through which clients can access resources in the API.

* Each route corresponds to a specific resource and supports one or more HTTP methods.

* For example, `/api/users` might be the base route for accessing user resources, with endpoints like `/api/users/{id}` to retrieve or update a specific user.

* Routes are typically organized hierarchically based on the structure of the underlying data model.

### REST Endpoints:

* REST endpoints are the specific URLs within a route that clients interact with to perform CRUD operations on resources.

* Endpoints are defined by combining the base route with additional path segments to identify the resource and the desired action.

* For example, `/api/users` might be the base route for accessing user resources, with endpoints like `/api/users/{id}` to retrieve or update a specific user.