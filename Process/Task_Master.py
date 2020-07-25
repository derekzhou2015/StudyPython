#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import random
import time
import queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass

def task_queue_callable():
    return task_queue

def result_queue_callable():
    return result_queue

def do_task_manager():
    QueueManager.register('get_task_queue', callable=task_queue_callable)
    QueueManager.register('get_result_queue', callable=result_queue_callable)

    manager = QueueManager(address=('192.168.50.130', 5000), authkey=b'abc')
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d..' % n)
        task.put(n)

    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=20)
        print('Result: %s ' % r)

    manager.shutdown()
    print('Master exit')
if __name__ == "__main__":
    do_task_manager()
print("----------------------------------")
