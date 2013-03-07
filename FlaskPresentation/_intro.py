# -*- coding: utf-8 -*-
"""
Web-development using Python with Flask

David McKeone - PyYYC - March 6, 2013
"""
from textwrap import dedent

from flask import Flask
from jinja2 import Markup

app = Flask(__name__)

@app.route('/')
def title():
    page = dedent(u"""\
        <html><head><title>Intro</title></head>
        <body>
        <h1>Web Development With Flask</h1>
        <br>
        <br>
        <br>
        <a href="/description">Let's Begin</a>
        </body>
        </html>"""
    )
    return Markup(page)


@app.route('/description')
def home():
    """
    This presentation is entirely in Python code.  Its intended to be entered by everyone so that
    learning can happen.

    I believe that the only true way to learn is to get your fingers on your keyboard.  You need to code, and
    then play. Put another way, this is a form of deliberate practice (Gladwell et. al) that helps us stretch our
    abilities and improve as programmers.

    Demos 1 through 8 will demonstrate various ways to use Flask.  After going through all of the demos a small
    coding dojo will take place where you will create a simple HTML Tic-Tac-Toe game.
    """
    page = dedent(u"""\
        <html><head><title>Description</title></head>
        <body>
        <h1>Web Development With Flask</h1>
        <h2>Who are you?</h2>
        <ul>
            <li>David McKeone</li>
            <li>~10 years as a professional programmer (C++, Python, Omnis Studio)</li>
            <li>
                I work at Arts Management Systems Ltd. making Theatre Manager, a box office management CRM for theatres
                (down with TicketMaster!)
            </li>
            <li>
                I'm a nomad.  I'm from Calgary, but I spent last year in London, and the year before
                in Paris and Nice.
            </li>
        </ul>
        <h2>What are we doing?</h2>
        <ul>
            <li>8 demos showing how to get started with Flask</li>
            <li>TDD/BDD Coding Dojo for a simple HTML Tic-Tac-Toe game (Time permitting)</li>
        </ul>
        <h2>Deliberate Practice (Outliers - Gladwell et. al)</h2>
        <ul>
            <li>Fingers on the keyboard</li>
            <li>Stretch our limits</li>
            <li>Continuous feedback</li>
            <li>Self-reflection</li>
        </ul>
        </body>
        </html>"""
    )
    return Markup(page)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
