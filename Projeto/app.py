import flask

from blueprints.docker_blueprint import docker_blueprint
from blueprints.jenkins_blueprint import jenkins_routes

app = flask.Flask(__name__)

app.register_blueprint(docker_blueprint)
app.register_blueprint(jenkins_routes)


@app.route('/')
def index():
    return flask.render_template('index.jinja')


if __name__ == '__main__':
    app.run(debug=True)
