#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import itertools
# count
natuals = itertools.count(5, 5)
for n in natuals:
    print(n)
    if n >= 10:
        break
print("----------------------------------")
# cycle
cs = itertools.cycle('kerwin')
for i, c in enumerate(cs):
    print(c)
    if i > 10:
        break
print("----------------------------------")
# cycls
ns = itertools.repeat('kerwin', 2)
for s in ns:
    print(s)
print("----------------------------------")
# takewhile
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))
print("----------------------------------")
# chain
chain = itertools.chain(['kerwin'], ['vicky'])
print(list(chain))
print("----------------------------------")
# groupby
group = itertools.groupby('AABCVDSDDSSSSssssee', lambda c: c.upper())
for key, grp in group:
    print(key, list(grp))
print("----------------------------------")


def pi(n):
    natuals = itertools.count(1, 2)
    ns = itertools.takewhile(lambda x: x <= 2*n-1, natuals)
    l = map(lambda x: 4/x if x % 4 == 1 else -4/x, ns)
    return sum(l)
#test
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
print("----------------------------------")