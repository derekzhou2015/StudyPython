#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import time,random
from datetime import datetime

def print_message_periodical(interval_seconds, message='keep alive'):
    while True:
        print('[MESSAGE][%s]:%s.' % (datetime.now(), message))
        start = time.time()
        end = start + interval_seconds
        while True:
            yield
            now = time.time()
            if now >= end:
                break


if __name__ == "__main__":
    pmp = print_message_periodical
    tasks = [pmp(1,'A'),pmp(5,'B'),pmp(10,'C')]
    while True:
        for task in tasks:
            next(task)