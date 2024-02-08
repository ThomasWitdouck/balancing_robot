#!/usr/bin/python

import socket
import sys
import time
import threading

mutex1 = threading.Lock()

# Check server ip address set
if len(sys.argv) < 2:
    raise RuntimeError('pass IP address of the server')

# Set the server address here like 1.2.3.4
SERVER_ADDR = sys.argv[1]

# These constants should match the server
BUF_SIZE = 10
SERVER_PORT = 4242
TEST_ITERATIONS = 1

# Open socket to the server
sock = socket.socket()
addr = (SERVER_ADDR, SERVER_PORT)
sock.connect(addr)

# Repeat test for a number of iterations
while 1:


    # First lock this code
    mutex1.acquire(1)

    # Read BUF_SIZE bytes from the server
    total_size = BUF_SIZE
    read_buf = b''
    while total_size > 0:
        buf = sock.recv(BUF_SIZE)
        print('read %d bytes from server' % len(buf))
        total_size -= len(buf)
        read_buf += buf

    # Check size of data received
    if len(read_buf) != BUF_SIZE:
        raise RuntimeError('wrong amount of data read %d', len(read_buf))

    # print data
    #integer_value = int.from_bytes(read_buf[0], byteorder='little')
    
    for i in range(BUF_SIZE):
        print(read_buf[i])

    # Send the data back to the server
    write_len = sock.send(read_buf)
    print('written %d bytes to server' % write_len)
    if write_len != BUF_SIZE:
        raise RuntimeError('wrong amount of data written')

    # Now unlock the code
    mutex1.release()

    time.sleep(1)
    

# All done
sock.close()
print("test completed")
