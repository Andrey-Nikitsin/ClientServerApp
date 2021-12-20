import socket
from dataclasses import dataclass, make_dataclass
from collections import namedtuple


DataServer = make_dataclass('DataServer',('SRV_HOST','SRV_PORT'))

@dataclass
class ClientServer(DataServer):

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

name_file = 'highway_to_hell.txt'

client = ClientServer("192.168.100.21", 7856)


if __name__ == '__main__':

    client.client_sock(name_file)