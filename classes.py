import socket
from RSA import encrypt, decrypt, generate_keys
from tkinter import Tk
from tkinter.filedialog import askopenfilename


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
        client_socket, client_address = server_socket.accept()
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

        Tk().withdraw()
        # Asking the server's user to insert a path to create a text file in.
        path = askopenfilename()

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
        exit(0)


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

    def recv_pub_key(self):
        """
        This function receives the public key in a string form
        and returns it in a tuple form.
        """

        my_socket = self.socket_operations()
        pub_key = my_socket.recv(1024).decode('utf-8')
        data = ''
        flag = True
        for i in range(1, len(pub_key) - 1):
            if ord(pub_key[i]) - ord('0') >= 0 and ord(pub_key[i]) - ord('0') <= 9:
                data += pub_key[i]
            elif flag:
                data += ','
                flag = False
        data = data.split(',')
        data = (int(data[0]), int(data[1]))
        pub_key = data
        my_socket.close()
        return pub_key

    def send_text_file(self):
        """
        This function receives a path and reads the data from the file in this path.
        It sends the data to the server in an encrypted form.
        """
        Tk().withdraw()
        # Asking the server's user to insert a path to create a text file in.
        path = askopenfilename()

        # Opening the file in a read mode.
        with open(path, mode='rt', encoding='utf-8') as f:

            # Creating the public key and preparing the socket.
            pub_key = self.recv_pub_key()
            my_socket = self.socket_operations()

            chunk_size = 5
            f_contents = f.read(chunk_size)
            # Reading the file's content until there is nothing to read.
            while True:
                if len(f_contents) == 0:
                    break
                # Encrypting the data, sending it to the server and reading the new data.
                f_contents = encrypt(f_contents, pub_key)
                my_socket.send(f_contents.encode('utf-8'))
                f_contents = f.read(chunk_size)
            my_socket.close()
        exit(0)
