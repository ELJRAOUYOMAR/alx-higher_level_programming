# 0x10. Python - Network #0

## Table of Contents
- [General](#general)
- [What a URL is](#what-a-url-is)
- [What HTTP is](#what-http-is)
- [How to read a URL](#how-to-read-a-url)
- [The scheme for a HTTP URL](#the-scheme-for-a-http-url)
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

## What HTTP is

HTTP (Hypertext Transfer Protocol) is the protocol used for transferring web pages on the internet. It defines how messages are formatted and transmitted, and how web servers and browsers should respond to various commands.

## How to read a URL

A URL consists of several components:
scheme://domain
/path?query_string#fragment_id


## The scheme for a HTTP URL

The scheme specifies the protocol used to access the resource. For HTTP URLs, the scheme is either `http` or `https`.

## What a domain name is

A domain name is a human-readable address used to identify a website. It maps to the IP address of the web server.

## What a sub-domain is

A sub-domain is a subset of a larger domain. For example, in `blog.example.com`, `blog` is a sub-domain of `example.com`.

## How to define a port number in a URL

A port number in a URL specifies the network port on the server to which the request is being sent. It follows the domain name and is separated by a colon. For example: `http://example.com:8080`.

## What a query string is

A query string is a part of a URL that contains data to be passed to web applications. It starts with a `?` and includes key-value pairs separated by `&`. For example: `http://example.com?name=value`.

## What an HTTP request is

An HTTP request is a message sent by the client to the server to request a resource. It includes the request line, headers, and an optional body.

## What an HTTP response is

An HTTP response is a message sent by the server to the client in response to an HTTP request. It includes the status line, headers, and an optional body.

## What HTTP headers are

HTTP headers are key-value pairs included in HTTP requests and responses. They provide metadata and control information. Common headers include `Content-Type`, `Content-Length`, `Authorization`, etc.

## What the HTTP message body is

The HTTP message body contains the data being transmitted in an HTTP request or response. It is optional and typically used with methods like POST or PUT.

## What an HTTP request method is

HTTP request methods indicate the desired action to be performed on a resource. Common methods include GET, POST, PUT, DELETE, etc.

## What an HTTP response status code is

HTTP response status codes indicate the result of the request. Common status codes include 200 (OK), 404 (Not Found), 500 (Internal Server Error), etc.

## What an HTTP Cookie is

An HTTP cookie is a small piece of data sent from the server and stored on the client side. Cookies are used to remember information about the user.

## How to make a request with cURL

cURL is a command-line tool for transferring data with URLs. To make a GET request:
```sh
curl http://example.com

To make a POST request:
curl -X POST -d "param1=value1&param2=value2" http://example.com

#what-happens-when-you-type-googlecom-in-your-browser

1. DNS Resolution: The browser resolves the domain name google.com to an IP address using DNS (Domain Name System).
2. TCP Connection: The browser establishes a TCP connection to the server at the resolved IP address.
3. HTTP Request: The browser sends an HTTP request to the server for the web page.
4. Server Response: The server processes the request and sends back an HTTP response with the requested resource (HTML, CSS, JS, images).
5. Rendering: The browser processes the response, renders the web page, and displays it to the user.



