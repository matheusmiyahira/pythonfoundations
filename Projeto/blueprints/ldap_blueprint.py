import flask
import ldap3

ldap_routes = flask.Blueprint(name='ldap',import_name='__name__',url_prefix='/login')

@ldap_routes.route('/')
def index():
    return flask.render_template('login.jinja')

@ldap_routes.route('/',methods=['POST'])
def login():
    usuario = flask.request.form['email']
    senha = flask.request.form['password']
    try:
        server = ldap3.server('ldap://localhost:389')
        client = ldap3.Connection(server, f'cn={usuario},dc=example,dc=org, senha')
        conectou = client.bind()
    except expression as identifier:
        print('Não foi possível conectar com o servidor.')
        conectou = 'Não foi possível conectar'

    return conectou