#!/usr/bin/env python3

import flask
import json

from usuarios.blueprint import usuarios_route # A IMPLEMETAR
from grupos.blueprint import usuarios_route # A IMPLEMETAR
from mensagens.blueprint import usuarios_route # A IMPLEMETAR

app = flask.Flask(__name__)
app.register_blueprint(usuarios_routes)
app.register_blueprint(grupos_routes)
app.register_blueprint(mensagens_routes)

@app.route('/')
def indedex():
    return None

if __name__=='__main__':
    app.run(debug=True)


