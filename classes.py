import socket
import os
import sys
from RSA import generate_prime_file, encrypt,decrypt, generate_keys


def check_file_path(path):
    if os.path.exists(path):
        print("A file already exists in this path. Would you like to overwrite it ?")
        will = input("Enter y for yes or n for no:\t")
        while will != 'y' and will != 'n':
            will = input("Please enter y for yes or n for no. Do not enter any other character:\t")
        if will == 'n':
            sys.exit()
        else:
            return 'continue'
    return 'continue'


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

    def prepare_keys(self):
        """
        This function prepares the keys for the server(priv_key) and for the
        client(pub_key). It sends to the client the pub_key and returns the priv_key.
        """

        client_socket = self.socket_operations()
        pub_key, priv_key = generate_keys()
        client_socket.send(str(pub_key).encode('utf-8'))
        client_socket.close()
        return priv_key

    def recv_text_file(self):
        """
        This function receives data from the client and writes it to
        a file.
        """

        # Asking the server's user to insert a path to create a text file in.
        path = input("Enter a path in which you would like to create a file:\t")
        if check_file_path(path):

            # Opening the file to a write mode.
            with open(path, mode='wt', encoding='utf-8') as f:
                # Preparing the keys and the client_socket.
                priv_key = self.prepare_keys()
                client_socket = self.socket_operations()

                data = client_socket.recv(1024).decode('utf-8')

                # Looping until the client sends no data.
                while True:
                    if not data:
                        break
                    # Decrypting the data, writing it to the file and "re-inputting it".
                    data = decrypt(data, priv_key)
                    f.write(data)
                    data = client_socket.recv(1024).decode('utf-8')
                client_socket.close()


class Client:
    def __init__(self, addr, host):
        """
        Constructor function.
        parameters: addr, host.
        addr: The IP address of the server.
        host: The port the server listens from.
        """

        self.addr = addr
        self.host = host

    def socket_operations(self):
        """
        This function tries to open the client's socket.
        If it opens successfully, it binds the socket to the server and returns the socket.
        Otherwise, it will print an error message and close the socket.
        """

        try:
            my_socket = socket.socket()
        except Exception as e:
            print("Socket could not be open! Check your network, Something went wrong in it")
            my_socket.close()
        else:
            my_socket.connect((self.addr, self.host))
            return my_socket


