#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
'a test class'
__author__ = 'Kerwin'

# arrary
arr = np.array(range(10, 20))
x = np.where(arr == 19)
print(x)
print('------------------------------------')
x = np.where(arr % 2 == 0)
print(x)
print('------------------------------------')
x = np.where(arr % 2 == 1)
print(x)
print('------------------------------------')
x = np.searchsorted(arr, 11)
print(x)
print('------------------------------------')
x = np.searchsorted(arr, 10, side='right')
print(x)
print('------------------------------------')
x = np.searchsorted(arr, [10, 11, 12])
print(x)
