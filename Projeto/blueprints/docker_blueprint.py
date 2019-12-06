import flask
import docker

docker_blueprint = flask.Blueprint(
    name='docker', import_name=__name__, url_prefix='/docker')


@docker_blueprint.route('/')
def index():
    try:
        client = docker.from_env()
        container = client.containers.get('9c116b418c')
        flask_app = {
            'id': container.short_id,
            'image': container.image.tags[0],
            'nome': container.name,
            'status': container.status
        }
    except Exception as e:
        flask_app = None
        # print(e)
    finally:
        return flask.render_template('docker.jinja', container=flask_app)


@docker_blueprint.route('/start')
def start():
    try:
        client = docker.from_env()
        container = client.containers.get('9c116b418c')
        container.start()
    except Exception as e:
        pass
    return(flask.redirect(flask.url_for('docker.index')))


@docker_blueprint.route('/stop')
def stop():
    try:
        client = docker.from_env()
        container = client.containers.get('9c116b418c')
        container.stop()
    except Exception as e:
        pass
    return(flask.redirect(flask.url_for('docker.index')))
