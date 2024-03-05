## API

### HTTP Verbs (HTTP Methods):

* GET: Retrieves data from the server. It should have no side effects on the server.

* POST: Submits data to the server to create a new resource.

* PUT: Updates an existing resource on the server.

* DELETE: Deletes a resource on the server.

* PATCH: Partially updates a resource on the server.

* HEAD: Retrieves headers from the server, similar to GET but without the response body.

* OPTIONS: Retrieves the HTTP methods that the server supports for a specified URL.

### HTTP Status Codes:

HTTP status codes are three-digit numbers that indicate the outcome of a client's request.
They are grouped into different categories:

* 1xx: Informational - Request received, continuing process.
* 2xx: Success - The action was successfully received, understood, and accepted.
* 3xx: Redirection - Further action needs to be taken to complete the request.
* 4xx: Client Error - The request contains bad syntax or cannot be fulfilled.
* 5xx: Server Error - The server failed to fulfill an apparently valid request.

### Common HTTP Status Codes:

* 200 OK: The request has succeeded.
* 201 Created: The request has been fulfilled, resulting in the creation of a new resource.
* 400 Bad Request: The server cannot process the request due to client error, such as malformed syntax.
* 401 Unauthorized: The request requires user authentication.
* 404 Not Found: The server cannot find the requested resource.
* 500 Internal Server Error: The server encountered an unexpected condition that prevented it from fulfilling the request.