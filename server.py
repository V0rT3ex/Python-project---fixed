from classes import Server
from GUI import main

def run():
   s = Server('127.0.0.1', 8820, 1)
   s.recv_text_file()

if __name__ == '__main__':
   # main()
   run()

