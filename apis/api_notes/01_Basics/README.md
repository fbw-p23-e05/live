# **5.01 API Basics**
## **Overview**
The aim of this submodule is to provide learners with an introduction to API fundamentals. Upon completion of the submodule, learners will have a clear understanding of what an API is, its purpose, the various types of APIs, and the REST verbs.

### Objectives

By the end of this submodule learner should be able to understand :
1. What is an API ?
2. Why we need API ?
3. What are the types of APIs ?
4. What are REST verbs and error codes ?\

**Key words**:
(API, Endpoint, HTTP methods, request, response, JSON, XML, REST, Authorization/authentication )\

**Resources**:
- [RedHat](https://www.redhat.com/en/topics/api)
- [IBM](https://www.ibm.com/topics/api)
- [Freecodecamp](https://www.freecodecamp.org/news/rest-vs-graphql-apis/)
- [Postman Docs](https://blog.postman.com/understanding-api-basics-beginners/)



## **What is an API ?**

- An API (Application Programming Interface) is a set of protocols and tools for building software applications.
- An API is a tool for building software applications that enables different components to communicate with each other.
- APIs define how software applications can share data and services.
- APIs can be used to build internal and external applications, automate business processes, and create new applications.
- APIs enable innovation and collaboration within an organization and with external partners and customers.
By providing access to their data and functionality, businesses can create new opportunities for value creation and differentiation in the marketplace.

## **Why we need APIs ?**
### **Business perspective**

From a business perspective, APIs are essential for a number of reasons:

- Integration and interoperability: APIs allow different software systems to communicate and share data, enabling businesses to integrate and streamline their operations. 
- New revenue streams: APIs allow businesses to create new revenue streams by opening up their platforms to third-party developers and partners. 
- Innovation and differentiation: APIs can be used to foster innovation and differentiation within an organization by enabling new ideas and products to be developed more quickly and easily. 

### **Technical perspective**

From a technical perspective, APIs are essential for a number of reasons:

- Standardization: APIs provide a standardized way for different software systems to communicate and share data, which can help to reduce complexity and improve interoperability.
- Scalability: APIs are designed to be scalable, meaning that they can handle large volumes of traffic and data without compromising performance or reliability.
- Security: APIs provide a secure way for different software systems to exchange data and functionality, with built-in authentication and authorization mechanisms to ensure that only authorized parties can access sensitive information.
- Flexibility: APIs can be customized and configured to meet the specific needs of different applications and systems, making them a flexible and adaptable solution for a wide range of use cases.

## **What are the types of APIs ?**
### **Public vs Internal APIs**
- Public APIs are developed for external developers and may have different security and governance requirements, while internal APIs are developed for internal use and may have stricter security and governance requirements.
- Internal APIs may use different technologies or frameworks depending on the needs of the organization.\


|              | Public APIs                              | Internal APIs                            |
|--------------|-----------------------------------------|-----------------------------------------|
| **Purpose**  | Designed for external developers or customers to access a company's services or data | Designed for internal use within an organization to enable different systems or applications to communicate with each other |
| **Accessibility** | Generally made available to the public   | Generally not exposed to the public      |
| **Authentication** | May require authentication or API keys to access | May require stricter authentication or authorization to access |
| **Governance**   | May be subject to different governance and security requirements than internal APIs | May be subject to more stringent governance and security requirements |
| **Examples** | Twitter API, Google Maps API, Stripe API | Salesforce API, Amazon Web Services API, Netflix API |

## **API types**

### **OS APIs**
Operating system (OS) APIs are provided by the OS to enable developers to interact with and control the OS.
- They allow software applications to access OS functionality such as process management, file system access, networking, device drivers, and security.
- Some common examples of OS APIs are Process management APIs, File system APIs, Networking APIs, Device Driver APIs, Security APIs
 **Examples** :
    - Windows API
    - POSIX API for Unix-like operating systems
    - macOS API
    - Android API
### **Library APIs**
A library API is pre-written code that programmers can use to perform common tasks, organized into libraries.
- Saves time and effort by allowing developers to reuse code.
- Examples include standard libraries, third-party libraries, and frameworks.
- Standard libraries are built into programming languages.
- Third-party libraries are developed by third-party vendors or open-source communities.
- Frameworks provide a complete set of tools and APIs for developing applications. 
 **Examples** :
    - Pandas
    - Numpy
    - OpenGL
    - TensorFlow    
### **Web APIs**
Web APIs are typically designed to be accessed using standard web protocols, such as HTTP, and use common data exchange formats such as JSON or XML to transfer data between the client and server.

- RPC:
    - RPC stands for Remote Procedure Call.
    - It is a protocol for communication between two systems, where a client can call a remote function on a server and receive a response.
    - The client and server use a predefined interface to communicate, which typically involves a specific set of function calls and parameters.
    - RPC is often used in distributed systems and is typically implemented using specific protocols like XML-RPC, JSON-RPC, or gRPC.

- [SOAP](https://www.soapui.org/):
    - SOAP stands for Simple Object Access Protocol.
    - It is an XML-based protocol for exchanging structured information between systems.
    - SOAP defines a standard messaging framework that can be used to exchange information between applications, regardless of the underlying operating system or programming language.
    - SOAP messages are typically transported over HTTP, SMTP, or other application layer protocols.
    - SOAP can be used to implement RPC-style communication, as well as more complex message exchange patterns like publish-subscribe.

- [REST](https://restfulapi.net/):
    - REST stands for Representational State Transfer.
    - It is a software architectural style that defines a set of constraints to be used when creating web services.
    - RESTful web services use HTTP methods (GET, POST, PUT, DELETE) to access and manipulate resources (e.g. data, files) identified by URIs.
    - RESTful APIs are typically lightweight and easy to use, and can be implemented using a variety of programming languages and frameworks.
    - RESTful APIs are often used in modern web applications and mobile apps, as they provide a simple and scalable way to expose data and functionality to clients.

- [GraphQL](https://graphql.org/):
    - GraphQL is a query language and runtime for APIs.
    - In January 2015, Facebook announced its internal APIs would be built on a new technology (though already in development since 2011)
    - GRAPHQL is essentially RPC, with good ideas from REST/HTTP mixed in
    - It provides a more flexible and efficient alternative to RESTful APIs, as clients can specify exactly what data they need and the server responds with only that data.
    - With GraphQL, the client defines the shape of the response, rather than the server.
    - GraphQL also provides powerful tooling for exploring and testing APIs, as well as client libraries for a variety of programming languages.
    - GraphQL can be used with any backend technology and is often used in modern web and mobile applications.

## **REST APIs verbs/ Error codes and Endpoints**
REST APIs (Representational State Transfer APIs) are designed to communicate over the HTTP protocol, and use standard HTTP methods, also known as verbs, to indicate the type of action to be performed on a resource.\
**REST API Endpoints:**\
Endpoints are the URLs that identify resources and the actions that can be taken on them. 
| HTTP Verb | CRUD Operation | Success Status Codes | Failure Status Codes | Description | REST API Endpoint |
| --- | --- | --- | --- | --- | --- |
| GET | Read | 200 OK | 404 Not Found, 401 Unauthorized, 403 Forbidden | Retrieve a resource from the server. | /resource/{resource_id}} |
| POST | Create | 201 Created | 400 Bad Request, 401 Unauthorized, 403 Forbidden | Create a new resource on the server. | /resource |
| PUT | Update | 200 OK | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found | Update an existing resource on the server. | /resource/{resource_id}} |
| DELETE | Delete | 204 No Content | 401 Unauthorized, 403 Forbidden, 404 Not Found | Delete a resource from the server. | /resource/{resource_id}} |
| PATCH | Update | 200 OK | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found | Partially update an existing resource on the server. | /resource/{resource_id}} |