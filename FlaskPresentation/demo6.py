# -*- coding: utf-8 -*-
"""

More Jinja2 template fun...

David McKeone - PyYYC - March 6, 2013
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/true")
def conditional_true():
    return render_template("conditional.html", message=u"Conditional Template", condition=True)

@app.route("/false")
def conditional_false():
    return render_template("conditional.html", message=u"Conditional Template", condition=False)

@app.route("/countdown")
def countdown():
    return render_template("countdown.html", counter=xrange(10, 0, -1))

@app.route("/block")
def block():
    return render_template("child.html", title=u"My Title", content=u"This is how you do blocks")

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )


