#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
'a test class'
__author__ = 'Kerwin'

from random import uniform
from functools import reduce

'''
i - Int
b - Bool
u - UInt
f - Float
c - 复合浮点数
m - timedelta
M - datetime
O - Object
S - String
U - Unicode String
V - 固定的其他类型的内存块 ( void )
'''

# arrary
arr = np.array(range(10))
print(arr.dtype)
print('------------------------------------')

arr = np.array([chr(n) for n in range(65, 91)])
print(arr, arr.dtype)
print('------------------------------------')
arr = np.array(range(10), dtype='S')
print(arr, arr.dtype, arr[0].decode('utf-8'))
print('------------------------------------')
arr = np.array(['Kerwin', 'Vicky', 'Lee'], dtype='S')
print(arr, arr.dtype)
print('------------------------------------')
arr = np.array(['Kerwin', 'Vicky', 'Lee'], dtype='S3')
print(arr, arr.dtype)
print('------------------------------------')
try:
    arr = np.array(['Kerwin', 1, 2], dtype='i')
    print(arr, arr.dtype)
except ValueError as e:
    print(e)
print('------------------------------------')
# astype
arr = np.array([round(float(n) + uniform(0, 1), 2) for n in range(10)])
print(arr, arr.dtype)
arr1 = arr.copy().astype(int)
print(arr1, arr1.dtype)
arr2 = arr1.copy().astype(bool)
print(arr2, arr2.dtype)
print('------------------------------------')
# copy
arr = np.array(range(10))
arr2 = arr.copy()
arr2 = map(lambda x: x * x, arr2)
print(arr, list(arr2))
print('------------------------------------')
# view
arr = np.array(range(10))
arr2 = arr.view()
for n in arr2:
    arr2[n] = n + 5
print(arr, arr2)
print('------------------------------------')
# base
arr = np.array(range(10))
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)
print('------------------------------------')
# shape (D,NUM)
arr = np.array([range(5), range(5, 10)])
print(arr.shape)

arr = np.array([range(5)], ndmin=5)
print(arr, arr.shape)
