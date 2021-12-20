import socket
import os
from dataclasses import dataclass

@dataclass()
class LocalServer:
    SRV_HOST: str
    SRV_PORT: int

    def serv_sock(self):
        serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)# SO_REUSEADDR - сбрасывает тайм аут
        serv_socket.bind((self.SRV_HOST, self.SRV_PORT))
        serv_socket.listen(8)
        return serv_socket

    def get_file(self, name_file):
        files = os.listdir()
        if name_file in files:
            print(name_file)
            return True
        else:
            return False

    def run_server(self):
        while True:
            connect, adress = self.serv_sock().accept()
            print(connect)
            data = connect.recv(2048)
            name_file = data.decode('utf-8')
            print(name_file)
            if self.get_file(name_file) == True:
                connect.send('1'.encode('utf-8'))
                with open(f'./{name_file}', 'rb') as file:
                    connect.sendfile(file, 0)
            else:
                answer = 'file no'
                connect.send(answer.encode('utf-8'))

            connect.close()


server = LocalServer("192.168.100.21", 7856)

if __name__ == '__main__':
    server.run_server()