#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import threading
import time
import socket
from sys import argv


def demo1():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 8080))
    s.send(b'GET /data.json HTTP/1.1\r\nHost: 127.0.0.1\r\nConnection: close\r\n\r\n')
    buffer = []
    while True:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    header, html = [item.decode('utf-8')
                    for item in data.split(b'\r\n\r\n', 1)]
    print(header)
    print(html)


print("----------------------------------")


def tcplink(sock, addr):
    print('Accpet new connection from %s:%s...' % addr)
    sock.send(b'Webcome.')
    while True:
        data = sock.recv(1024)
        if data == b'exit':
            sock.send(data)
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


def service():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    s.listen(5)
    print('Waitting for connection...')
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()


def send_handler(scok):
    print('Please send content."exit" to quit.')    
    while True:
        content = input('Msg\\>:')    
        scok.send(content.encode('utf-8'))
        if content == 'exit':
            break

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 9999))
    print(s.recv(1024).decode('utf-8'))

    t = threading.Thread(target=send_handler, args=(s,))
    t.start()
    while True:
        data = s.recv(1024).decode('utf-8')
        if data == 'exit':
            break
        print(data)

    print('Goodbye.')
print("----------------------------------")
if __name__ == "__main__":
    if '-d1' in argv:
        demo1()
    elif '-s' in argv:
        service()
    elif '-c' in argv:
        client()
print("----------------------------------")
