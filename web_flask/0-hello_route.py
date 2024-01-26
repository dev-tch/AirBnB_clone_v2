#!/usr/bin/python3
""""
first module flask
"""
from flask import Flask


# create flast application
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    return message hello when web server invoking router '/'
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
