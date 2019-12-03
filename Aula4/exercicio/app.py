#!/usr/bin/python3
import flask

from blueprint.random_blueprint import random_blueprint
from blueprint.nome_blueprint import nome_blueprint

app = flask.Flask(__name__)
app.register_blueprint(random_blueprint)
app.register_blueprint(nome_blueprint)

app.run(debug=True)

