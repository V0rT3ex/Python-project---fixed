import socket
import os
import sys
from RSA import generate_prime_file, encrypt,decrypt, generate_keys


class Server:
    def __init__(self, addr, port, listens):
        """
        Constructor function.
        parameters: addr, port, listens.
        addr: The IP address of the server.
        port: The port the server listens from.
        listens: Amount of clients the server listens to.
        """

        self.addr = addr
        self.port = port
        self.listens = listens

    def socket_operations(self):
        """
        This function creates the server's socket and the client's socket,
        it binds the server's socket to the address and port passed in the init method,
        listens to the amount of clients and returns the client's socket.
        """
        server_socket = socket.socket()
        server_socket.bind((self.addr, self.port))
        server_socket.listen(self.listens)
        client_socket, client_address =server_socket.accept()
        return client_socket
