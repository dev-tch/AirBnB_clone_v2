#!/usr/bin/python3
"""
module web application flask
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def get_cities_by_states():
    """
    pass list states to view
    """
    states = storage.all('State').values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
