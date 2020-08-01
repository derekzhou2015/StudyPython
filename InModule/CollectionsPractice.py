#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap,Counter
from time import sleep
import os
import argparse
Point = namedtuple('Point', ['x', 'y'])
Circle = namedtuple('Circle', ['x', 'y', 'r'])
p = Point(150, 150)
c = Circle(5, 5, 10)
print(p, c)
print("----------------------------------")
l = [i for i in range(10)]
d = deque(l)
d.append(100)
d.appendleft(-100)
print(d)
d.pop()
d.popleft()
print(d)
print("----------------------------------")
d = dict(name='kerwin', age=37, gender='male')
#d1 = {'name': 'vicky', 'age': 30, 'gender': 'female'}
dd = defaultdict(lambda: None, **d)
print(dd['hobby'], dd['name'], dd)
print("----------------------------------")
l = [(chr(k), k-96) for k in range(97, 123)]
dd = OrderedDict(l)
print(type(dd), type(d))
print(dd, d)
print(list(d.keys()))
print(list(dd.keys()))

print("----------------------------------")


class LastUpdateOrderDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('Removed:', last)
        if containsKey:
            del self[key]
            print('Set:', (key, value))
        else:
            print('Add', (key, value))
        OrderedDict.__setitem__(self, key, value)


lud = LastUpdateOrderDict(10)

for item in range(97, 123):
    lud[chr(item)] = item
print(lud)

print("----------------------------------")
defaults = {
    'color': 'red',
    'user': 'guest'
}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}
combined = ChainMap(command_line_args, os.environ, defaults)
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])
print(command_line_args)
print("----------------------------------")

c = Counter()
for ch in 'Kerwin Zhou keke':
    c[ch] = c[ch] + 1
print(c)
print("----------------------------------")
