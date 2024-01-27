#!/usr/bin/python3
"""
    A script that starts a Flask web application:

    The web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of the text
        variable (replace underscore _ symbols with a space )
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """Returns Hello HBNB"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Return a formated text"""
    txt = text.replace("_", " ")
    return ("C {}".format(txt))


@app.route('/python')
@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """display Python followed by the value of the text variable"""
    txt = text.replace("_", " ")
    return ("Python {}".format(txt))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display 'n is a number' only if n is an interger"""
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n=None):
    """display a HTML page only if n is an integer"""
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run()
