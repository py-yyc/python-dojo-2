# -*- coding: utf-8 -*-
"""
Flask is easy to test too!

David McKeone - PyYYC - March 6, 2013
"""
import unittest

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_hello(self):
        response = self.client.get('/')
        self.assertEquals("Hello World", response.data)


if __name__ == '__main__':
    unittest.main()
