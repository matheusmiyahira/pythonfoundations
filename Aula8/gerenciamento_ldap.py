#!/usr/bin/env python3

import ldap3
from hashlib import md5
from binascii import b2a_base64

username = 'admin'
password = 'admin'

server = ldap3.Server('ldap://localhost:389')

client = ldap3.Connection(server,f'cn={username},dc=example,dc=org', password)

client.bind()
# print(client)


# INSERINDO USUARIO

md5json = md5('senhaSuperSegura'.encode('utf-8')).digest()

user = {
    'cn':'cleiton',
    'sn':'rasta',
    'mail':'aosom.dequem@cleitonrasta.com.br',
    'uidNumber':'1000',
    'gidNumber':'1000',
    'uid':'cleiton.rasta',
    'homeDirectory':'/home/joao',
    'userPassword':'{MD5}' + b2a_base64(md5json).decode('utf-8')
}

objectClass = ['top','person','organizationalPerson','inetOrgPerson', 'posixAccount']
cn = 'uid=' + user['mail'] + ',dc=example,dc=org'
# print(client.add(cn,objectClass,user))


# PESQUISANDO USUARIO
email = 'aosom.dequem@cleitonrasta.com.br'
dn = 'uid=' + email + ',dc=example,dc=org'
# client.search(dn,'(objectclass=person)',attributes=['cn','sn'])
# print(client.entries)


# ALTERANDO USUARIO
changes = {
    'cn': [(ldap3.MODIFY_REPLACE, ['xuxa'])],
    'sn': [(ldap3.MODIFY_REPLACE, ['meneguel'])]
}
# client.modify(dn,changes)
# print(client.result)

# DELETANDO USUARIO
# print(client.delete(dn))