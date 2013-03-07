# -*- coding: utf-8 -*-
"""

There are many ways do return data from a Flask function.

David McKeone - PyYYC - March 6, 2013
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"  # Returns 200 OK

@app.route("/notfound")
def not_found():
    return "404 Not Found", 404  # Returns 404 NOT FOUND

@app.route("/template")
def template():
    """
    Flask is integrated with a fast, easy-to-use templating system, Jinja2. (http://jinja.pocoo.org/)

    Performance comparison with other Python templating systems:
    http://stackoverflow.com/questions/1324238/what-is-the-fastest-template-system-for-python
    """
    return render_template("message.html", message=u"Hello World")

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )


