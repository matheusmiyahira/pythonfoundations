import paramiko

client = paramiko.client.SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('127.0.0.1',username='developer',password='4linux')

#standard input, stantdard output, standard error
stdin, stdout,stderr = client.exec_command('ls -la')

# ESCREVENDO
# stdin.write('Escrevendo\n')
# stdin.flush()

if stdout.channel.recv_exit_status() == 0:
    print(stdout.read().decode('utf-8'))
else:
    print(stderr.read().decode('utf-8'))

