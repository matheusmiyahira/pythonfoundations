#!/usr/bin/env python3

# virtualenv -p python3 env
# . env/bin/activate
# pip install flask

import flask

app = flask.Flask(__name__)
app.run()
