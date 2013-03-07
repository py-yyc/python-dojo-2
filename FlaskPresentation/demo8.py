# -*- coding: utf-8 -*-
"""

Sessions and Forms with POST-back

NOTE: Take a look at itsdangerous (https://github.com/mitsuhiko/itsdangerous) if using HTTP Sessions with Flask

David McKeone - PyYYC - March 6, 2013
"""
from flask import Flask, request, session, render_template
from jinja2 import Markup

app = Flask(__name__)

# Required for Session handling
app.config['SESSION_COOKIE_NAME'] = "PyYYC_Flask_Demo8"
app.config['SECRET_KEY'] = "Shhh..ItsASecret"

GET = "GET"
POST = "POST"
NUMBER_KEY = 'number'
ITEMS_KEY = 'items'

@app.route('/', methods=[GET, POST])
def home():
    error = None
    success = None

    # Check for POST data
    if request.method == POST:
        # Check that we have an appropriate POST
        try:
            entered = request.form[NUMBER_KEY]
        except KeyError:
            error = (u"Page error.  The form didn't submit the required input 'number'.  Please tell the developer of "
                     u"this page he sucks, nicely though.")
            entered = None

        if entered:
            # Attempt to add the number
            try:
                # Is it an integer?
                entered = int(entered)
            except ValueError:
                # Maybe a float?
                try:
                    entered = float(entered)
                except ValueError:
                    error = u"I don't think '{}' is a number.  Please enter a number.".format(entered)
                    entered = None

        if entered:
            try:
                # KeyError may occur when ITEMS_KEY has not yet been created
                items = session[ITEMS_KEY]
                # AttributeError may occur when ITEMS_KEY exists, but the value does not have an append method
                items.append(entered)
                # Assign back into session
                session[ITEMS_KEY] = items

                success = u"Successfully added {}".format(entered)
            except (KeyError, AttributeError):
                # Both exceptions require creating a new session ITEMS_KEY with a value of a single-list with
                # the new number.
                session[ITEMS_KEY] = [entered]

    # Display the session
    return render_template(
        "form.html",
        items=session.get(ITEMS_KEY, None),
        error=error,
        success=success
    )

@app.route('/clear')
def clear():
    """
    Clear the current HTTP session (a.k.a clear the cookie)
    """
    try:
        del session[ITEMS_KEY]
    except KeyError:
        # Session data is already gone, nothing to do.
        pass

    # NOTE: Markup() denotes that HTML tags are permitted within the text (Otherwise they are escaped)
    return render_template(
        "child.html",
        title=Markup(u"Ghostrider, the <span style=\"text-decoration:line-through;\">pattern is full</span>"
                     u" session is clear.")
    )

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )


