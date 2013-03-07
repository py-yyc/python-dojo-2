# -*- coding: utf-8 -*-
"""
Flask app for Tic-Tac-Toe, Xs and Os, or Naughts and Crosses.

Make a layout similar to: http://ostermiller.org/calc/tictactoe.html (a table based grid)

Rules:
- There are two players
- The game is played on a 3x3 grid
- The 'X' player goes first
- The two players take turns to place their mark in one empty square on the grid
- The first player marks their squares on a grid with the 'X'
- The second player marks their squares on a grid with the 'O'
- Goal is to be the first player to get three of their marked squares in a row (straight, or diagonal)
- If all spaces are used up and there is no winner, then the game is declared a draw
"""

# ????

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("board.html", message=u"Hello World")

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )



