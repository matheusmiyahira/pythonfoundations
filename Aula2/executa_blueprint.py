import flask
from blueprint import usuarios

app = flask.Flask(__name__)
app.register_blueprint(usuarios)

app.run()