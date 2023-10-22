#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """display a HTML page with state list fetch frome storage"""
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """display a HTML page with state city from state id fetch frome storage"""
    states = storage.all("State").values()
    for state_by_id in states:
        if state_by_id.id == id:
            state = state_by_id
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def SQLsession_close(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
