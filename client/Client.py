import socket

SRV_HOST = "127.0.0.6"
SRV_PORT = 7856

set_file = ''

clients = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients.connect((SRV_HOST, SRV_PORT))
take_file = 'highvay_to_hell.txt'
clients.send(take_file.encode('utf-8'))
data = clients.recv(2048)
answer_server = data.decode('utf-8')
if answer_server == '1':
    data = clients.recv(2048)
    text_from_file = data.decode("utf-8")
    set_file+=text_from_file
    with open(f'{take_file}', 'w') as file:
        file.write(set_file)
else:
    print(answer_server)