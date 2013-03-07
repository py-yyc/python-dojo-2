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

from flask import Flask, request, session, render_template
from jinja2 import Markup

app = Flask(__name__)

# Required for Session handling
app.config['SESSION_COOKIE_NAME'] = "PyYYC_Flask_tictactoe"
app.config['SECRET_KEY'] = "Shhh..ItsASecret"

GET = "GET"
POST = "POST"
GAME_DATA = 'game_data'
PLAYER = 'player'
MESSAGE = 'message'
ENDED = 'ended'

@app.route('/')
def game():
	session[GAME_DATA] = [[''] * 3, [''] * 3, [''] * 3]
	session[PLAYER] = 'X'
	session[MESSAGE] = ''
	session[ENDED] = False

	return render_template(
		'tictactoe.html',
		data = session[GAME_DATA]
	)

@app.route('/', methods=[POST])
def move():
	game_data = session[GAME_DATA]
	player = session[PLAYER]
	position = request.form['position']
	row, col = position.split('-')
	row = int(row)
	col = int(col)

	if not session[ENDED] and not game_data[row][col]:
		game_data[row][col] = session[PLAYER]

	if any((
		any(all(col == player for col in row) for row in game_data),
		any(all(col == player for col in row) for row in zip(*game_data[::-1])),
		all((game_data[0][0] == player, game_data[1][1] == player, game_data[2][2] == player)),
		all((game_data[0][2] == player, game_data[1][1] == player, game_data[2][0] == player))
	)):
		session[MESSAGE] = 'Player %s wins!' % session[PLAYER]
		session[ENDED] = True

	session[PLAYER] = 'X' if session[PLAYER] == 'O' else 'O'

	return render_template(
		'tictactoe.html',
		data = session[GAME_DATA],
		message = session[MESSAGE]
	)

if __name__ == '__main__':
	app.run(
		host='0.0.0.0',
		port=5000,
		debug=True
	)
