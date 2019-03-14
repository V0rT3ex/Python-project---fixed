from classes import Server

def main():
   s = Server('127.0.0.1', 8820, 1)
   s.recv_text_file()


if __name__ == '__main__':
   main()

