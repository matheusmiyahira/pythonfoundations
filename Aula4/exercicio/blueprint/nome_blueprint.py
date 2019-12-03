import flask

nome_blueprint = flask.Blueprint('nome',__name__,url_prefix='/nome')

@nome_blueprint.route('/', methods=['GET'])
def index():
    # html = '<html><head></head><body>'
    # html += '<form action="" method="post">'
    # html += '<label for="nome" id="nome_label">Insira seu nome:'
    # html += '</label>'
    # html += '<input id="nome" name="nome">'
    # html += '<input type="submit" value="OK">'
    # html += '</form>'
    # html += '</body></html>'
    # return html
    return flask.render_template('index.html')

@nome_blueprint.route('/', methods=['POST'])
def welcome():
    return f'Ola {dict(flask.request.form)["nome"]}, Seja bem vindo!'

