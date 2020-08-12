#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import threading
import time
import asyncio
from sys import argv

PORT = 80

async def hello(s):
    print('Hello World. %s (%s)' % (s, threading.currentThread()))
    await asyncio.sleep(2)
    print('Hello Again. %s (%s)' % (s, threading.currentThread()))



async def wget(host):
    print('[SYS_MESSAGE] Web get host: %s ...' % host)
    connect = asyncio.open_connection(host,PORT)
    reader,writer = await connect
    header = 'GET / HTTP/1.1 \r\nHOST:%s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('[RES_MESSAGE]  HOST:%s HEADER > %s ' % (host,line.decode('utf-8').rstrip()))
    writer.close()
    

if __name__ == "__main__":
    if len(argv) < 2:
        loop = asyncio.get_event_loop()
        tasks = [hello('task1'), hello('task2'), hello('task3')]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()
    elif '-w' in argv:
        loop = asyncio.get_event_loop()
        tasks = [wget(host) for host in ['www.baidu.com','www.sina.com.cn','www.163.com','www.sohu.com']]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()