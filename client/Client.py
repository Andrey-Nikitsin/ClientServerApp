import socket


class ClientServer():

    def __init__(self,SERVER_HOST,SERVER_PORT):
        self.SRV_HOST = SERVER_HOST
        self.SRV_PORT = SERVER_PORT

    def client_sock(self, name_file):
        set_file = ''
        clients = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clients.connect((self.SRV_HOST, self.SRV_PORT))
        take_file = name_file
        clients.send(take_file.encode('utf-8'))
        data = clients.recv(2048)
        answer_server = data.decode('utf-8')
        if answer_server == '1':
            print('there is a file - sending')
            data = clients.recv(2048)
            text_from_file = data.decode("utf-8")
            set_file += text_from_file
            with open(f'{take_file}', 'w') as file:
                file.write(set_file)
        else:
            print('no such file exists')

client = ClientServer("127.0.0.6", 7856)

name_file = 'highway_to_hell.txt'

if __name__ == '__main__':
    client.client_sock(name_file)
