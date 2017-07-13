# -*- coding:utf-8 -*-
import bottle
import flask

bottle_app = bottle.app()
flask_app = flask.Flask(__name__)


@bottle_app.route('/')
@flask_app.route('/')
def index():
    return b"Hello, World"


def wsgi(env, start):
    c = b"Hello, World"
    start("200 OK", [('Content-Type', 'text/plain'), ('Content-Length', str(len(c)))])
    return [c]
