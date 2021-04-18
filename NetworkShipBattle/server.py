import socket
import sys
from _thread import start_new_thread


class Server:
    def __init__(self, host, port, max_number_of_clients):
        self.port = port
        self.host = host
        self.max_number_of_clients = max_number_of_clients
        self.connection_status = True
        self.server_sock = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)

    def start_thread(self, connection):
        ''' Excecuted each time a client is connecting '''
        connection.send(str.encode(
            f"SERVER: Client connected to server {self.host} on port {self.host}"))
        while True:
            try:
                data = connection.recv(2048)
                response = data.decode("utf-8")
                if data:
                    print("SERVER: Received from client =>", response)
                else:
                    print("SERVER: Disconnected from server")
                    break
                connection.sendall(str.encode(response))  # security
            except socket.error:
                sys.stderr.write("SERVER : Start thread failed")
                break
        self.close_connection(connection)

    def server_initialisation(self):
        ''' connect IP to Port
        start_new_thread start a new thread and return its identifier.
        The thread will call the function with positional arguments from the tuple args
        '''
        try:
            self.server_sock.bind((self.host, self.port))
            self.server_sock.listen(self.max_number_of_clients)
            print("SERVER: the server is waiting for new connections ...")
        except socket.error as e:
            print(
                "SERVER: Error the server has not been initialized => => ", e)
        while self.connection_status:
            try:
                connection, address = self.server_sock.accept()  # processus bloquant
                print(
                    f"SERVER: Client connected to: adresse IP {address[0]}, port {address[1]}")
                start_new_thread(self.start_thread, (connection,))
            except socket.error as e:
                print("SERVER: Client rejected:    ", e)

    def close_connection(self, connection):
        connection.close()
        print("SERVER : connection closed")


s = Server("127.0.0.1", 8080, 3)
s.server_initialisation()
