#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
def call_sum(*l):
    def sum():
        return reduce(lambda x,y: x + y,l)
    return sum

l = list(range(10))
f = call_sum(*l)
print(f())

l = list(range(10,20))
f = call_sum(*l)
print(f())
print("----------------------------------")
def createCounter():
    i = 0
    def counter():
        nonlocal i
        i += 1
        return i
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
print("----------------------------------")
