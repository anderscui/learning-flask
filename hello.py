# coding=utf-8
from __future__ import absolute_import, unicode_literals, division

from flask import Flask
from flask import request, current_app, g, session

app = Flask(__name__)


@app.route('/')
def index():
    # view func
    return '<h1>Hello World!</h1>'


@app.route('/about')
def about():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p' % user_agent


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s!</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)
