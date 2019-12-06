#!/usr/bin/env python3

import ldap3
from hashlib import md5
from binascii import b2a_base64

username = 'admin'
password = 'admin'

server = ldap3.Server('ldap://localhost:389')
client = ldap3.Connection(server, f'cn={username},dc=exemplo,dc=org',password)

client.bind()
print(client)


# Inserindo usuario

md5json = md5('superSenhaSegura',encode('utf-8')).digest()

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
