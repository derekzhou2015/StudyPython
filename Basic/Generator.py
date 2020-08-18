#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable,Iterator
g = (item for item in range(10))
print(g)
print("----------------------------------")
#斐波拉契数列
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield(b)
        a,b = (b,a+b)
        n += 1

for item in fib(5):
    print(item)
print("----------------------------------")
#杨辉三角
def triangles(max):
    L,n = [1],0
    yield L
    while n<max:
        L=[([0]+L)[m]+(L+[0])[m] for m in range(len(L)+1)]
        yield L
        n += 1
g = triangles(10)
for item in g:
    print(item)
print("----------------------------------")
l = [1,2,3,4,5]
print(isinstance(l,Iterator),isinstance(l,Iterable),isinstance(iter(l),Iterator))
print("----------------------------------")