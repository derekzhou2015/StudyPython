#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
from sys import argv
import os
import time
import random
import threading
import multiprocessing

if len(argv) == 1:
    exit()
param = argv[1][1:]

balance = 0
lock = threading.Lock()

print(multiprocessing.cpu_count())
print("----------------------------------")

def loop():
    print('Thread %s is running.' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('Thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(random.random() * 2)
    print('Thread %s ended.' % threading.current_thread().name)


if __name__ == '__main__' and param == 's1':
    print('Thread %s is running.' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('Thread %s ended.' % threading.current_thread().name)


def chanage_it(n):
    # push first after get out.result is zero.
    global balance
    balance += n
    balance -= n


def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            chanage_it(n)
        finally:
            lock.release()

if __name__ == '__main__' and param == 's2':
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
print("----------------------------------")