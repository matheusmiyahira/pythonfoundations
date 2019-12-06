
Error no windows de acesso a pasta
```
PS C:\Users\cardosm6\Documents\DevEnv\pythonfoundations\Projeto> docker-compose up -d
Creating projeto_jenkins_1 ... error

ERROR: for projeto_jenkins_1  Cannot create container for service jenkins: b'Drive sharing seems blocked by a firewall'

ERROR: for jenkins  Cannot create container for service jenkins: b'Drive sharing seems blocked by a firewall'
ERROR: Encountered errors while bringing up the project.
PS C:\Users\cardosm6\Documents\DevEnv\pythonfoundations\Projeto>
```
```
PS C:\Users\cardosm6\Documents\DevEnv\pythonfoundations\Projeto> docker rm -f $(docker ps -qa)
97260148257c
PS C:\Users\cardosm6\Documents\DevEnv\pythonfoundations\Projeto> docker run -dit -p 8080:8080 -v ./dados_jenkins:/var/jenkins_home --name jenkins jenkins/jenkins
```





#### Autenticando Jenkins
```
(pythonfoundations) C:\Users\cardosm6\Documents\DevEnv\pythonfoundations\Projeto>docker exec -it jenkins_py cat /var/jenkins_home/secrets/initialAdminPassword
122265d41a5f4d64b029baa7c76b84d5



(pythonfoundations) C:\Users\cardosm6\Documents\DevEnv\pythonfoundations\Projeto>
```

