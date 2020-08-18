#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from numpy import random
from functools import reduce
'a test class'
__author__ = 'Kerwin'

# arrary
arr = np.array(range(10))
sum = reduce(lambda x, y: x+y, arr)
print(sum)
print('------------------------------')
arr1 = np.array(range(5))
arr2 = np.array(range(5, 10))
z = []
for x, y in zip(arr1, arr2):
    z.append(x+y)
print(z)
print('------------------------------')
z = np.add(arr1, arr2)
print(z, z[0])
