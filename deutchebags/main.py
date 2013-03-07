from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def mark():
    board = [[''] * 3] * 3
    return render_template('board.html', board=board)

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )