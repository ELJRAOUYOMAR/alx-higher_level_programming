# README

## Table of Contents
- [General](#general)
- [What a URL is](#what-a-url-is)
- [What HTTP is](#what-http-is)
- [How to read a URL](#how-to-read-a-url)
- [The scheme for an HTTP URL](#the-scheme-for-an-http-url)
- [What a domain name is](#what-a-domain-name-is)
- [What a sub-domain is](#what-a-sub-domain-is)
- [How to define a port number in a URL](#how-to-define-a-port-number-in-a-url)
- [What a query string is](#what-a-query-string-is)
- [What an HTTP request is](#what-an-http-request-is)
- [What an HTTP response is](#what-an-http-response-is)
- [What HTTP headers are](#what-http-headers-are)
- [What the HTTP message body is](#what-the-http-message-body-is)
- [What an HTTP request method is](#what-an-http-request-method-is)
- [What an HTTP response status code is](#what-an-http-response-status-code-is)
- [What an HTTP Cookie is](#what-an-http-cookie-is)
- [How to make a request with cURL](#how-to-make-a-request-with-curl)
- [What happens when you type google.com in your browser](#what-happens-when-you-type-googlecom-in-your-browser)

## General

This README provides an overview of basic web concepts and how they interact to enable web communication. It covers URLs, HTTP, domain names, HTTP headers, cookies, and making requests with cURL.

## What a URL is

A URL (Uniform Resource Locator) is the address used to access resources on the web. It specifies the location of a resource and the protocol to retrieve it.

### Example
https://www.example.com/path/to/resource?query=example#fragment


In this example:
- `https` is the scheme.
- `www.example.com` is the domain.
- `/path/to/resource` is the path.
- `query=example` is the query string.
- `fragment` is the fragment.

## What HTTP is

HTTP (Hypertext Transfer Protocol) is the protocol used for transferring web pages on the internet. It defines how messages are formatted and transmitted, and how web servers and browsers should respond to various commands.

### Example
When you type `http://example.com` in your browser, your browser sends an HTTP request to the server, and the server responds with the requested web page.

## How to read a URL

A URL consists of several components:
scheme://domain
/path?query_string#fragment_id


### Example
For the URL `https://www.example.com:8080/search?q=example#section1`:
- `https` is the scheme.
- `www.example.com` is the domain.
- `8080` is the port number.
- `/search` is the path.
- `q=example` is the query string.
- `section1` is the fragment.

## The scheme for an HTTP URL

The scheme specifies the protocol used to access the resource. For HTTP URLs, the scheme is either `http` or `https`.

### Example
- `http://example.com`
- `https://secure.example.com`

## What a domain name is

A domain name is a human-readable address used to identify a website. It maps to the IP address of the web server.

### Example
- `example.com`
- `google.com`

## What a sub-domain is

A sub-domain is a subset of a larger domain. It is used to organize and navigate to different sections of a website.

### Example
- `blog.example.com` (where `blog` is a sub-domain of `example.com`)
- `store.example.com` (where `store` is a sub-domain of `example.com`)

## How to define a port number in a URL

A port number in a URL specifies the network port on the server to which the request is being sent. It follows the domain name and is separated by a colon.

### Example
- `http://example.com:8080` (where `8080` is the port number)
- `https://example.com:443` (where `443` is the port number, typically used for HTTPS)

## What a query string is

A query string is a part of a URL that contains data to be passed to web applications. It starts with a `?` and includes key-value pairs separated by `&`.

### Example
- `http://example.com/search?q=test&page=2` (where `q=test` and `page=2` are query parameters)

## What an HTTP request is

An HTTP request is a message sent by the client to the server to request a resource. It includes the request line, headers, and an optional body.

### Example
```sh
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```


## What an HTTP response is

An HTTP response is a message sent by the server to the client in response to an HTTP request. It includes the status line, headers, and an optional body.

### Example
```sh
HTTP/1.1 200 OK
Date: Mon, 05 Jul 2021 12:00:00 GMT
Server: Apache/2.4.1
Content-Type: text/html
Content-Length: 1234

<!DOCTYPE html>
<html>
<body>
<h1>Hello, world!</h1>
</body>
</html>
```
#what-http-headers-are
HTTP headers are key-value pairs included in HTTP requests and responses. They provide metadata and control information.

Example
Request headers:
```sh
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```
Response headers:
```sh
Content-Type: text/html
Content-Length: 1234
Server: Apache/2.4.1
```

#what-the-http-message-body-is
The HTTP message body contains the data being transmitted in an HTTP request or response. It is optional and typically used with methods like POST or PUT.
### Example
Request body for a POST request:

```sh
POST /submit-form HTTP/1.1
Host: www.example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 27

name=John&age=30&city=New+York
```

#what-an-http-request-method-is
HTTP request methods indicate the desired action to be performed on a resource. Common methods include:
- GET: Retrieve data from the server.
- POST: Submit data to be processed by the server.
- PUT: Update or create a resource on the server.
- DELETE: Delete a resource on the server.

### Example
```sh
GET /index.html HTTP/1.1
POST /submit-form HTTP/1.1
PUT /update-resource HTTP/1.1
DELETE /delete-resource HTTP/1.1
```

#what-an-http-response-status-code-is
HTTP response status codes indicate the result of the request. Common status codes include:

- 200 OK: The request was successful.
- 404 Not Found: The requested resource could not be found.
- 500 Internal Server Error: The server encountered an error processing the request.
### Example
```sh
HTTP/1.1 200 OK
HTTP/1.1 404 Not Found
HTTP/1.1 500 Internal Server Error
```

#what-an-http-cookie-is

An HTTP cookie is a small piece of data sent from the server and stored on the client side. Cookies are used to remember information about the user.

### Example
Setting a cookie:
```sh
Set-Cookie: sessionId=abc123; Path=/; HttpOnly
```
Sending a cookie with a request:
```sh
Cookie: sessionId=abc123
```

#how-to-make-a-request-with-curl
cURL is a command-line tool for transferring data with URLs.

### Example
To make a GET request:
```sh
curl http://example.com
```
To make a POST request:
```sh
To make a POST request:
```
#what-happens-when-you-type-googlecom-in-your-browser
Steps:
1. DNS Resolution: The browser resolves the domain name google.com to an IP address using DNS (Domain Name System).
2. TCP Connection: The browser establishes a TCP connection to the server at the resolved IP address.
3. HTTP Request: The browser sends an HTTP GET request to the server for the web page.
4. Server Response: The server processes the request and sends back an HTTP response with the requested resource (HTML, CSS, JS, images).
5. Rendering: The browser processes the response, renders the web page, and displays it to the user.

Example
When you type google.com:

1. DNS resolves to 142.250.190.78.
2. The browser establishes a TCP connection to 142.250.190.78.
3. The browser sends:

```sh
GET / HTTP/1.1
Host: www.google.com
```
4. The server responds:
```sh
HTTP/1.1 200 OK
Content-Type: text/html
...
<html>...Google homepage...</html>
```
5. The browser renders and displays the Google homepage.


## cURL
cURL (Client for URLs) is a command-line tool used for transferring data with URLs. It supports a variety of protocols including HTTP, HTTPS, FTP, and more. cURL is commonly used to make HTTP requests, upload files, and interact with RESTful APIs. Below are some key aspects and examples of using cURL.

#### Basic cURL Commands
1. Make a GET Request

The simplest use of cURL is to fetch a URL.
```sh
curl http://example.com
```
This command fetches the content of http://example.com and displays it in the terminal.

2. Make a POST Request

You can use cURL to send data to the server using the POST method.
```sh
curl -X POST -d "param1=value1&param2=value2" http://example.com
```
This sends a POST request to http://example.com with the specified data.

3. Send JSON Data

To send JSON data, you need to set the content type header and pass the data in JSON format.
```sh
curl -X POST -H "Content-Type: application/json" -d '{"key1":"value1", "key2":"value2"}' http://example.com
```
4. Set Headers

You can specify custom headers to be sent with your request.
```sh
curl -H "Authorization: Bearer YOUR_TOKEN" http://example.com
```

5. Download a File

To download a file from a URL, you can use the -O option.
```sh
curl -O http://example.com/file.zip
```
This downloads file.zip from the specified URL to the current directory.

6. Follow Redirects
If the URL you are accessing redirects to another URL, you can use the -L option to follow the redirects.
```sh
curl -L http://example.com
```
7. Save Output to a File

You can save the output of a cURL request to a file using the -o option.
```sh
curl -o output.html http://example.com
```

8. Show Response Headers

To see the headers of the response, you can use the -I option.
```sh
curl -I http://example.com
```

### Authentication
1. Basic Authentication

For endpoints that require basic authentication, you can pass the username and password using the -u option.
```sh
curl -u username:password http://example.com
```

2. Bearer Token

For endpoints that require a bearer token, you can set the Authorization header.
```sh
curl -H "Authorization: Bearer YOUR_TOKEN" http://example.com
```


### Debugging
1. Verbose Mode

To see detailed information about the request and response, you can use the -v option.
```sh
curl -v http://example.com
```
2. Include Response Headers

To include the response headers in the output, you can use the -i option.
```sh
curl -i http://example.com
```
### Advanced Usage
1. Upload a File

To upload a file, you can use the -F option to specify the file and field name.
```sh
curl -F "file=@/path/to/file.txt" http://example.com/upload
```
2.Send Multiple Headers

To send multiple headers, you can use multiple -H options.
```sh
curl -H "Header1: value1" -H "Header2: value2" http://example.com
```

3. Limit Transfer Rate

You can limit the transfer rate using the --limit-rate option.
```sh
curl --limit-rate 100k http://example.com
```
cURL is a powerful tool with a wide range of options and capabilities. It is widely used for testing APIs, automating tasks, and debugging network issues.



