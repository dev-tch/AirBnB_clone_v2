#!/usr/bin/python3
""""
first module flask
"""
from flask import Flask


# create flast application
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def get_hello_hbnb():
    """
    return message 'hello HBNB!'
    when web server invoking router '/'
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def get_hbnb():
    """
    return message HBNB
    when web server invoking router '/hbnb'
    """
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
