import flask
import ldap3
from hashlib import md5
from binascii import b2a_base64

ldap_routes = flask.Blueprint(name='ldap',import_name=__name__,url_prefix='/login')

@ldap_routes.route('/')
def index():
    return flask.render_template('login.jinja')

@ldap_routes.route('/',methods=['POST'])
def login():
    email = flask.request.form['email']
    senha = flask.request.form['password']

    try:
        server = ldap3.Server('ldap://localhost:389')
        client = ldap3.Connection(server,f'cn=admin,dc=example,dc=org','admin')
        conectou = client.bind()

        pass_md5 = md5(senha.encode('utf-8')).digest()
        pass_md5 = '{MD5}' + b2a_base64(pass_md5).decode('utf-8')

        dn = 'uid='+ email + ',dc=example,dc=org'

        client.search(dn,'(objectclass=person)',attributes=['mail','userPassword'])

        if(pass_md5 == client.entries[0].userPassword.value.decode('utf-8')):
            flask.session['logged'] = True
            print('Encontrou')
            return(flask.redirect('/'))
        else:
            print('Não encontrou')
            return(flask.redirect(flask.url_for('ldap.index')))
    except Exception as e:
        print('Não foi possível conectar com o servidor', e)
        conectou = client.bind()