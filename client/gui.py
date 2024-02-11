
import sys

from tkinter import *
from tkinter import ttk

from tcp_client import *


# Check server ip address set
if len(sys.argv) < 2:
    raise RuntimeError('pass IP address of the server')

# Set the server address here like 1.2.3.4
SERVER_ADDR = sys.argv[1]

# These constants should match the server
BUF_SIZE_SEND = 2
BUF_SIZE_RECV = 10
SERVER_PORT = 4242
TEST_ITERATIONS = 1

sock = openClient(SERVER_ADDR, SERVER_PORT)


gui = Tk()
frm = ttk.Frame(gui, padding=10)
frm.grid()
ttk.Label(frm, text="Balancing Robot").grid(column=0, row=0)
ttk.Button(frm, text="Send/read", command=writeRead(sock, BUF_SIZE_SEND, BUF_SIZE_RECV)).grid(column=1, row=0)

def exit():
    closeClient(sock)
    gui.destroy()
    

ttk.Button(frm, text="Exit", command=exit).grid(column=2, row=0)

gui.mainloop()