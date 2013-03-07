# -*- coding: utf-8 -*-
"""
The Web Server Gateway Interface defines a simple and universal interface between web servers and
web applications or frameworks for the Python programming language.
(http://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)


WSGI is the foundation of most Python web applications.  This is a basic WSGI application

David McKeone - PyYYC - March 6, 2013
"""
from wsgiref.simple_server import make_server

def hello_world(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])  # HTTP Status, List of 2-Tuples for Response Headers
    return ["Hello World!"]

if __name__ == '__main__':
    srv = make_server('0.0.0.0', 5000, hello_world)  # "hello_world" is your app
    srv.serve_forever()