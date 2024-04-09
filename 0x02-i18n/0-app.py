from flask import Flask, render_template

"""A flask module"""

app = Flask(__name__)


@app.route('/')
def index() -> html:
    """
    Route the index page
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
