#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
'a test class'
__author__ = 'Kerwin'

# arrary
# 1D to 2D
arr = np.array(range(10))
newarr = arr.reshape(2, 5)
print(newarr)
print('------------------------------------')

# 1D to 3D
arr = np.array(range(20))
newarr = arr.reshape(2, 5, 2)
print(newarr, newarr.base)
print('------------------------------------')

# undefined
arr = np.array(range(20))
newarr = arr.reshape(2, 2, -1)
print(newarr)
print('------------------------------------')

# Flattening the arrays
arr = np.array([range(5), range(5, 10)])
newarr = arr.reshape(-1)
print(newarr)
print('------------------------------------')
