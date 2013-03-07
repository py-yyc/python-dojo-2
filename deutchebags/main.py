from flask import Flask, render_template, request

app = Flask(__name__)

GET = "GET"
POST = "POST"
BOARD_SIZE = 3

@app.route("/", methods=[GET, POST])
def mark():
    board = [[''] * BOARD_SIZE] * BOARD_SIZE
    if request.method == POST:
        for row_idx in range(BOARD_SIZE):
            for col_idx in range(BOARD_SIZE):
                form_element_id = "{row}-{col}".format(row=row_idx, col=col_idx)
                board[row_idx][col_idx] = request.form[form_element_id]
    return render_template('board.html', board=board)

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )