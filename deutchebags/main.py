from flask import Flask, render_template, request

app = Flask(__name__)

GET = "GET"
POST = "POST"
BOARD_SIZE = 3
X = 'Player1'
Y = 'Player2'


def detect_rows(board):
    for row in board:
        x_detected = True
        o_detected = True
        for item in row:
            if item != X:
                x_detected = False
            if item != Y:
                y_detected = False
        if x_detected:
            row = ['XX'] * 3
        if o_detected:
            row = ['YY'] * 3
        if x_detected or o_detected:
            return board, True
    return board, False


def detect_lines(board):
    # detect rows
    board, detected = detect_rows(board)
    if detected:
        return board

    # detect columns


    # detect diagonals


@app.route("/", methods=[GET, POST])
def mark():
    board = [[''] * BOARD_SIZE] * BOARD_SIZE
    if request.method == POST:
        for row_idx in range(BOARD_SIZE):
            for col_idx in range(BOARD_SIZE):
                form_element_id = "{row}-{col}".format(row=row_idx+1, col=col_idx+1)
                board[row_idx][col_idx] = request.form[form_element_id]
    return render_template('board.html', board=board)


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )