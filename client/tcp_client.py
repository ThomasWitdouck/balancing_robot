#!/usr/bin/python

import socket
import sys
import time
import threading

mutex1 = threading.Lock()

read_buf = b''
send_buf = bytes([1,0])

# Open socket to the server

def openClient(server_addr, server_port):
    sock = socket.socket()
    addr = (server_addr, server_port)
    sock.connect(addr)
    return sock


def writeRead(sock, size_send, size_recv):
    # First lock this code
    mutex1.acquire(1)

    # Send data to the server
    write_len = sock.send(send_buf)
    print('written %d bytes to server' % write_len)
    if write_len != size_send:
        raise RuntimeError('wrong amount of data written')

    # Read size_recv bytes from the server
    read_buf = b''
    total_size = size_recv
    while total_size > 0:
        buf = sock.recv(size_recv)
        print('read %d bytes from server' % len(buf))
        total_size -= len(buf)
        read_buf += buf

    # Check size of data received
    if len(read_buf) != size_recv:
        raise RuntimeError('wrong amount of data read %d', len(read_buf))

    # print data
    #integer_value = int.from_bytes(read_buf[0], byteorder='little')

    for i in range(size_recv):
        print(read_buf[i])

    # Now unlock the code
    mutex1.release()

def closeClient(sock):
    sock.close()
