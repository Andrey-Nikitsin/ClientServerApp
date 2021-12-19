import socket
import os

class LocalServer:

    def __init__(self,SERVER_HOST,SERVER_PORT):
        self.SRV_HOST = SERVER_HOST
        self.SRV_PORT = SERVER_PORT

    def serv_sock(self):
        serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serv_socket.bind((self.SRV_HOST, self.SRV_PORT))
        serv_socket.listen(8)
        return serv_socket

    def get_file(self, name_file):
        files = os.listdir()
        if name_file in files:
            return True
        else:
            return False

    def run_server(self):
        while True:
            connect, adress = self.serv_sock().accept()
            data = connect.recv(2048)
            name_file = data.decode('utf-8')
            if self.get_file(name_file) == True:
                connect.send('1'.encode('utf-8'))#отправляем ответ что файл есть
                with open(f'./{name_file}', 'r') as file:
                    response = file.read()
                connect.send(response.encode('utf-8'))
            else:
                answer = 'file no'
                connect.send(answer.encode('utf-8'))

            connect.close()


server = LocalServer("127.0.0.6",7856)

if __name__ == '__main__':
    server.run_server()