#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %d ...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    for n in range(5):
        print('[PRODUCER] Produce %d ...' % n)
        r = c.send(n + 1)
        print('[PRODUCER] Consumer return: %s ' % r)
    c.close()
c = consumer()
produce(c)