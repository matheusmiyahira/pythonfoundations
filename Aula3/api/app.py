#!/usr/bin/env python3

import flask
import json

from usuarios.blueprint import usuarios_route # A IMPLEMETAR

app = flask.Flask(__name__)
app.register_blueprint(usuarios_route)

@app.route('/')
def index():
    return None

if __name__=='__main__':
    app.run(debug=True)


