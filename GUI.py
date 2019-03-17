from tkinter import *
from classes import Server, Client


"""
This module is consist of a Graphical User Interface
(GUI) and uses the classes module I have built.
"""


def pack(*args):
    for item in args:
        item.pack()


def main():

    # Creating a blank window (root var)
    root = Tk()

    # Creating a frame
    frame = Frame(root)

    # Creating buttons
    button1 = Button(frame, text="Button1")
    button2 = Button(frame, text="Button2")
    button3 = Button(frame, text="Button3")
    button4 = Button(frame, text="Button4")



    # Packing the whole items
    pack(frame, button1, button2, button3, button4)

    # Making the window appear constantly
    root.mainloop()


if __name__ == '__main__':
    main()
