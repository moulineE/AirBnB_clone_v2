#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """display html 'Hello HBNB!'"""
    return "<p>Hello HBNB!</p>"


@app.route("/", strict_slashes=False)
def HBNB():
    """display html 'HBNB'"""
    return "<p>HBNB</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
