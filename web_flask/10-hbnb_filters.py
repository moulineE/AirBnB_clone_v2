#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def states():
    """
    display a HTML page like 6-index.html,
    """
    models = {
            "states": storage.all("State").values()
            "amenities": storage.all("Amenity").values()
            }
    return render_template('7-states_list.html', models=models)


@app.teardown_appcontext
def SQLsession_close(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
