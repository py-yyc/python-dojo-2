# -*- coding: utf-8 -*-
"""

Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.  (http://flask.pocoo.org)


This is a basic Flask application: Hello World.

David McKeone - PyYYC - March 6, 2013
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('0.0.0.0', 5000, app)
    srv.serve_forever()



