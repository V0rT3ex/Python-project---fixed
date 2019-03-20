from tkinter import *
from classes import Server, Client


"""
This module consists of a Graphical User Interface
(GUI) and uses the classes module I have built.
"""

client = None
server = None


def raise_frame(frame):
    frame.tkraise()


def proceed(frame, name, ip_entry, port_entry):
    ip = ip_entry.get()
    port = port_entry.get()
    if ip != '' and port != '':
        raise_frame(frame)
        title_label = Label(frame, text=name)
        title_label.grid(row=1)
        if name == 'Client':
            global client
            client = Client(ip, int(port))
            send_button = Button(frame, text="Send text file", command=client.send_text_file)
            send_button.grid(row=2)
        else:
            global server
            server = Server(ip, int(port), 1)
            recv_button = Button(frame, text="Receive text file", command=server.recv_text_file)
            recv_button.grid(row=2)


def details(frame, text, next_frame):
    raise_frame(frame)
    ip_label = Label(frame, text="IP:")
    port_label = Label(frame, text="Port:")
    ip_entry = Entry(frame)
    port_entry = Entry(frame)
    if text == "Client":
        client_label = Label(frame, text="Client")
        client_label.grid(row=1)
        proceed_button = Button(frame, text="Proceed", command=lambda: proceed(next_frame, "Client", ip_entry, port_entry))
    else:
        server_label = Label(frame, text="Server")
        server_label.grid(row=1)
        proceed_button = Button(frame, text="Proceed", command=lambda: proceed(next_frame, "Server", ip_entry, port_entry))

    ip_label.grid(row=2)
    port_label.grid(row=3)
    ip_entry.grid(row=2, column=1)
    port_entry.grid(row=3, column=1)
    proceed_button.grid(row=4)


def main():
    root = Tk()
    root.geometry('500x500')
    photo = PhotoImage(file="return.png")
    main_frame = Frame(root)
    server_frame = Frame(root)
    client_frame = Frame(root)
    last_frame = Frame(root)
    for frame in (main_frame, client_frame, server_frame, last_frame):
        frame.grid(row=0, column=0, sticky='news')

    # main_frame:
    main_label = Label(main_frame, text="Choose client of server:")
    main_label.pack()
    client_button = Button(main_frame, text="Client", command=lambda: details(client_frame, "Client", last_frame))
    server_button = Button(main_frame, text="Server", command=lambda: details(server_frame, "Server", last_frame))

    return_button = Button(client_frame, image=photo, command=lambda: raise_frame(main_frame))
    return_button.grid(row=0)
    return_button = Button(server_frame, image=photo, command=lambda: raise_frame(main_frame))
    return_button.grid(row=0)

    # Laying-out
    client_button.pack()
    server_button.pack()

    raise_frame(main_frame)
    root.mainloop()


if __name__ == '__main__':
    main()
