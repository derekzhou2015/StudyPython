#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import random
import time
import queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


def do_task_worker():
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    manager = QueueManager(address=('192.168.50.130', 5000), authkey=b'abc')
    manager.connect()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        try:
            n = task.get(timeout=1)
            print("Run task %d * %d ..." % (n, n))
            r = '%d * %d = %d' % (n, n, n*n)
            time.sleep(1)
            result.put(r)

        except queue.Empty:
            print('Task queue is empty.')
    print('Worker exit')


if __name__ == "__main__":
    do_task_worker()
print("----------------------------------")
