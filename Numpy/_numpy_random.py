#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from numpy import random
'a test class'
__author__ = 'Kerwin'

# arrary
arr = random.randint(10)
print(arr)
print('------------------------------------')
arr = random.rand()
print(arr)
print('------------------------------------')
arr = random.randint(100, size=(10))
print(arr)
print('------------------------------------')
arr = random.randint(100, size=(10, 5))
print(arr)
print('------------------------------------')
arr = random.rand(4, 2)
print(arr)
print('------------------------------------')
arr = random.choice(range(10), size=(5))
print(arr)
print('------------------------------------')
arr = random.choice(range(10), size=(5, 2))
print(arr)
print('------------------------------------')
