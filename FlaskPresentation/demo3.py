# -*- coding: utf-8 -*-
"""

Werkzeug also has a WSGI server with a built-in debugger.  Flask can use it directly.  It isn't for production.

David McKeone - PyYYC - March 6, 2013
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/error")
def error():
    a = u"My Variable"
    b = 7269767679
    raise ValueError("Oh noes!")

@app.route("/change")
def change():
    return "Change me!"

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )


