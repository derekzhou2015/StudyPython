#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
'a test class'
__author__ = 'Kerwin'

# arrary
arr = np.array([range(5), range(5, 10)])
for x in np.nditer(arr):
    print(x)
print('------------------------------------')

# different datatype
arr = np.array(range(5))
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)
print('------------------------------------')

# different step
arr = np.array([range(5), range(5, 10)])
for x in np.nditer(arr[:, ::3]):
    print(x)
print('------------------------------------')

# ndenumerate
arr = np.array(range(5))
for idx, x in np.ndenumerate(arr):
    print(idx, ":", x, arr[idx])
