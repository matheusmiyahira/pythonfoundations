#!/usr/bin/env python3

# virtualenv -p python3 env
# . env/bin/activate
# pip install flask

import flask
# import emoji

# print(emoji.emojize('Python is :thumbsup:', use_aliases=True))

app = flask.Flask(__name__)

dados = {
    'acesso':'Ok',

}

# CONFIGURANDO ROTAS
@app.route('/')
def index():
    return flask.jsonify(dados)

# Buscar informacao sobre decorators
# def x():
#     return 'Oi2'

@app.route('/teste/<string:nome>/meusarquivos', methods=['GET', 'POST'])
def teste(nome):
    return f'Testes retornando {nome} meus arquivos'

@app.route('/<int:id>', methods=['POST'])
def index_get_id(id):
    dados = { 'nome' : f'nome do id {id}' }
    return flask.jsonify(dados)
# para testar $ curl -X POST http://localhost:5000/12

@app.route('/teste/teste')
def teste_teste():
    return 'teste teste'

app.run(host='0.0.0.0', debug=True, port=80)
