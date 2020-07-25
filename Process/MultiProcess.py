#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
from multiprocessing import Process, Queue, Pool
from sys import argv
from subprocess import call
import os,time,random

if len(argv) == 1 :
    exit()

param = argv[1][1:]
def run_proc(name):
    print('Run child process %s(%s)...' % (name, os.getpid()))


if __name__ == '__main__' and param == 's1':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('ChildProc',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')


def long_time_task(name):
    print('Run task %s (%s)...' % (name,os.getpid()))
    st = time.time()
    time.sleep(random.random() * 3)
    et = time.time()
    print('Task %s runs %0.2f seconds.' % (name,et-st))

if __name__ == '__main__' and param == 's2':
    print('Parent process %s .' % os.getpid())
    p = Pool()
    for i in range(9):
        p.apply_async(long_time_task,args=(i,))
    print('Waitting for subprocesses done...')
    p.close()
    p.join()
    print('All processes done.')

if __name__ == '__main__' and param == 's3':
    print('$ nslookup www.python.org')
    r = call(['nslookup','www.python.org'])
    print('Exit code:',r)