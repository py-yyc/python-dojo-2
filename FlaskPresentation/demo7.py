# -*- coding: utf-8 -*-
"""

Routes with variables

David McKeone - PyYYC - March 6, 2013
"""
from flask import Flask

app = Flask(__name__)

@app.route('/<folder>/<int:item_id>')
def folders(folder, item_id):
    """
    General folder route
    """
    return u"You asked for id {} in the {} folder.".format(item_id, folder)

@app.route('/number/<int:num>')
def root(num):
    """
    Specialized route for number folder
    """
    return u"You said number {}.".format(num)

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )


