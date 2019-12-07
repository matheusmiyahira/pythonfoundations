import flask
import ldap3

ldap_routes = flask.Blueprint(name='ldap',import_name='__name__',url_prefix='/ldap')

@ldap_routes.route('/')
def index():
    return flask.render_template('login.jinja')

@ldap_routes.route('/login',methods=['POST'])
def login():
    return flask.request.form
