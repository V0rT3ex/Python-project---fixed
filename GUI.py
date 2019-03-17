from tkinter import *
from classes import Server, Client


"""
This module is consist of a Graphical User Interface
(GUI) and uses the classes module I have built.
"""


def pack(*args, side=None):
    for item in args:
        item.pack(side)


def main():

    # Creating a blank window (root var)
    root = Tk()

    # Making the window appear constantly
    root.mainloop()


if __name__ == '__main__':
    main()
