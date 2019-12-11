import requests

token = '2BCwQNaz4VzLfEKsrp8A'

projetos = requests.get(f'http://localhost:81/api/v4/projects?private_token={token}')
print(projetos.json())

projeto = {
    'name':'batata-frita'
}

projetos = requests.post(f'http://localhost:81/api/v4/projects?private_token={token}',projeto)


projetos = requests.get(f'http://localhost:81/api/v4/users?private_token={token}')

usuario= {
    'email':'daniel.silva@4linux.com.br',
    'username':'daniel.silva',
    'name':'Daniel Silva',
    'password':'4linux123'
}
projetos = requests.post(f'http://localhost:81/api/v4/users?private_token={token}',usuario)

project_id = 1
pessoa = {
    'user_id':12,
    'access_level':40
}

projetos = requests.post(f'http://localhost:81/api/v4/projects/{project_id}?private_token={token}',pessoa)

