#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import socket
from sys import argv

def service():
    port = 9999
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(('127.0.0.1',port))
    print('Bind UDP on %d....' % port)

    while True:
        data,addr = s.recvfrom(1024)
        print('Received from %s:%s' % addr)
        s.sendto(b'Hellow,%s.' % data,addr)
        if data == b'shutdown':
            break

    print('Unbind UDP on %d...' % port)
print("----------------------------------")

def client():
    addr = ('127.0.0.1',9999)
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    for data in [b'Kerwin',b'Lee',b'Vicky',b'shutdown']:
        s.sendto(data,addr)
        print(s.recv(1024).decode('utf-8'))
    s.close()

print("----------------------------------")
if __name__ == "__main__":
    if '-c' in argv:
        client()
    elif '-s' in argv:
        service()
