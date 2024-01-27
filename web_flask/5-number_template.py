#!/usr/bin/python3
""""
first module flask
"""
from flask import Flask, render_template


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


@app.route('/c/<text>', strict_slashes=False)
def get_c_text(text):
    """
    passing parameters  in flask rounting
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/', strict_slashes=False,
           defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def get_python__text(text):
    """
    passing parameters  in flask rounting
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def get_number_n(n):
    """
    return int value
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def get_number_template_n(n):
    """
    pass variable to template htmp
    """
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
