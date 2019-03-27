from classes import Client
from GUI import main


def run():
   c = Client('127.0.0.1', 8820)
   c.send_text_file()


if __name__ == '__main__':
   # run()
   main()


