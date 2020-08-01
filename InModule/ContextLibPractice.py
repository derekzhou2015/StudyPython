#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'

from contextlib import contextmanager,closing
from urllib.request import urlopen
class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s' % self.name)


with Query('Kerwin') as q:
    q.query()

print("----------------------------------")


class Query2(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query2(name)
    yield q
    print('Exit')

with create_query('Vicky') as q:
    q.query()
print("----------------------------------")
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)

with tag('div'):
    print('Hello')
    print('Vicky')
print("----------------------------------")

with closing(urlopen('http://127.0.0.1')) as page:
    for line in page:
        print(line)

print("----------------------------------")
@contextmanager
def closing_custom(thing):
    try:
        yield thing
    except:
        thing.close()


with closing_custom(urlopen('http://127.0.0.1')) as page:
    for line in page:
        print(line)
print("----------------------------------")
