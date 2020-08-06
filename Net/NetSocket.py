#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import threading
import time
import socket
from sys import argv

HEADER = 64
PORT = 9999
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

#-----------Utility------------------
def message_format(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    return send_length,message

#-----------Service------------------
def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            msg_length,message = message_format(msg)
            conn.send(msg_length)
            conn.send(message)   

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f'[{addr}]{msg}')

    conn.close()


def service():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    print(f'[STARTING] server is starting...')
    server.listen(5)
    print(f'[LISTENING] Server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS {threading.activeCount() - 1}]')

    

#-----------Client------------------

def handle_client_send(conn):
    print(f'[TIPS] Please send your messages.')
    connected = True
    while connected:
        msg = input('[SEND]:')
        msg_length,message = message_format(msg)
        conn.send(msg_length)
        conn.send(message)
        if msg == DISCONNECT_MESSAGE:
            connected = False


def handle_client_recv(conn):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length :
            msg_length = int(msg_length)
            message = conn.recv(msg_length).decode(FORMAT)
            print(f'[RECV]:{message}')
            if message == DISCONNECT_MESSAGE:
                connected = False
            

def client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    thread_send = threading.Thread(target=handle_client_send, args=(client,))
    thread_recv = threading.Thread(target=handle_client_recv, args=(client,))
    thread_send.start()
    thread_recv.start()
    thread_send.join()
    thread_recv.join()

    print('[DISCONNECT] Disconnected.')

#-----------------------------
if __name__ == "__main__":
    if '-s' in argv:
        service()
    elif '-c' in argv:
        client()

