#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import threading

local_school = threading.local()


def process_student():
    std = local_school.student
    print('Hello,%s(in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    local_school.student = {'name':name}
    process_student()


t1 = threading.Thread(target=process_thread, args=('kerwin',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('lee',), name='Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()
print("----------------------------------")



