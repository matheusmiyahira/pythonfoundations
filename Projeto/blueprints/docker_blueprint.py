import flask
import docker

docker_routes = flask.Blueprint(name='docker',import_name=__name__,url_prefix='/docker')

@docker_routes.route('/')
def index():
    if not flask.session['logged']:
        return flask.redirect(flask.url_for('ldap.index'))
    try:
        client = docker.from_env()
        container = client.containers.get('80f1dbe8d865')
        flask_app = {
            'id':container.short_id,
            'imagem': container.image.tags[0],
            'nome': container.name,
            'status':container.status
        }
    except Exception as e:
        flask_app = {}
    
    finally:
        return flask.render_template('docker.jinja', container=flask_app)

@docker_routes.route('/start')
def start():
    if not flask.session['logged']:
        return flask.redirect(flask.url_for('ldap.index'))
    try:
        client = docker.from_env()
        container = client.containers.get('80f1dbe8d865')
        container.start()
    except Exception:
        pass
    return flask.redirect(flask.url_for('docker.index'))

@docker_routes.route('/stop')
def stop():
    if not flask.session['logged']:
        return flask.redirect(flask.url_for('ldap.index'))
    try:
        client = docker.from_env()
        container = client.containers.get('80f1dbe8d865')
        container.stop()
    except Exception:
        pass
    return flask.redirect(flask.url_for('docker.index'))