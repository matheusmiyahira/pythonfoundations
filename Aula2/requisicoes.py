#!/usr/bin/env python3

# def vermelho(retorno_funcao):
#     def modificaCor(retorno_funcao):
#         return f'\033[91m{retorno_funcao}\033[0m'
#     return modificaCor

# @vermelho
# def texto(texto):
#     return texto

# print(texto('Uma palavra'))

import requests

# data = {
#     "name":"Abner"
# }

# res = requests.get('http://gen-net.herokuapp.com/api/users', params=data)
# print(res.json())




res = requests.post('http://localhost/12')
res = res.json()
# print(res['nome'])
print(res)
