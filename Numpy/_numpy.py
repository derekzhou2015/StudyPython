#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
'a test class'
__author__ = 'Kerwin'

# arrary
arr = np.array(range(10))
print(type(arr), arr)
print('------------------------------------')
# 1-D
arr = np.array(61)
print(type(arr), arr)
print('------------------------------------')
# 2-D
arr = np.array([range(10), range(10, 20)])
print(type(arr), arr, arr[0][0])
print('------------------------------------')
# 3-D
arr = np.array([[range(10), range(10, 20)], [range(20, 30), range(30, 40)]])
print(type(arr), arr, arr[1][0][0])
print(arr.ndim)
print('------------------------------------')
# 5-d
arr = np.array([range(10), range(10)], ndmin=5)
print(type(arr), arr, arr.ndim)
print('------------------------------------')

# last item
arr = np.array(range(10))
print(type(arr), arr, arr[-1])
print('------------------------------------')
arr = np.array(range(10))
print(arr[0:])
print(arr[1:4])
print(arr[:5])
print(arr[-3:-1])
print('------------------------------------')
# step
print(arr[1:5:2])
print(arr[::2])
print('------------------------------------')
# split 2-D
arr = np.array([range(5), range(5, 10)])
print(arr[1, 1:4])
print(arr[0:2, 2])
print(arr[0:2, 0:2])
print('------------------------------------')
