import socket
import sys


class Network_connection:
    def __init__(self):
        # self.host = "192.168.1.17"
        self.host = "127.0.0.1"
        self.port = 8080
        self.client_sock = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        #print(self.start_connection)

    def start_connection(self):
        try:
            self.client_sock.connect((self.host, self.port))
            self.server_response = self.client_sock.recv(
                2048).decode()  # security
            print(self.server_response)
            return self.server_response
        except socket.error:
            sys.stderr.write("CLIENT: Connection failed")

    def send_data_to_server(self, data):
        try:
            return self.client_sock.send(str.encode(data))
        except socket.error as e:
            print("CLIENT: Failure to send data: ", e)

    def display_reveived_data_from_server(self):
        try:
            print("CLIENT: Sent to server =>  ",
                  self.client_sock.recv(2048).decode())
            return self.client_sock.recv(2048).decode()
        except socket.error as e:
            print("CLIENT: Failure to receive data:  ", e)

    def send_data_to_server_and_keep_open_connection(self, data):
        total_send_data = 0
        while total_send_data < len(data):
            sent_data = self.client_sock.send(
                str.encode(data[total_send_data:]))
            if sent_data == b"":
                raise RuntimeError("socket connection broken")
            total_send_data = total_send_data + sent_data

    def receive_data_from_server_and_keep_open_connection(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < 2048:
            chunk = self.client_sock.recv(
                min(2048 - bytes_recd, 2048)).decode()
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        result = b''.join(chunks)
        print(result)
        return result


n = Network_connection()
n.start_connection()
# n.send_data_to_server_and_keep_open_connection("hello server")
# n.receive_data_from_server_and_keep_open_connection()
n.send_data_to_server("Hey server")
n.display_reveived_data_from_server()
