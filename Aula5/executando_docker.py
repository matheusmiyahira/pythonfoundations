#!/usr/bin/env python3

import docker

# client = docker.Docker("tcp://127.0.0.1:2376") #conecxão remota
client = docker.from_env()  # conecxão local
# client.containers.run('ubuntu:latest','echo Hello World!') # buscando imagem do ubuntu
# buscando imagem do python
# print(client.containers.run('python', 'python --help'))
all_containers = client.containers.list()
print(type(all_containers[0]))
print(all_containers)
container = client.containers.get('9c116b418c')
print(container.short_id)
print(container.name)
print(container.image.tags)
