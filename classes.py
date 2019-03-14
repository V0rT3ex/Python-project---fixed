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

