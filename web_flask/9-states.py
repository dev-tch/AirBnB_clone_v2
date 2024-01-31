#!/usr/bin/python3
"""
module web application flask
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def get_states():
    """
    pass list states to view
    """
    states = storage.all('State').values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def get_state_by_id(id):
    """
    pass state object to view based on id param
    """
    states = storage.all('State').values()
    stateObj = None
    for state in states:
        if state.id == id:
            stateObj = state
            break
    return render_template('9-states.html', stateObj=stateObj)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
