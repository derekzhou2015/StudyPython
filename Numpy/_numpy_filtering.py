#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from random import randint
'a test class'
__author__ = 'Kerwin'

# arrary
arr = np.array(range(10))
fil = [bool(randint(0, 1)) for x in range(10)]
result = arr[fil]
print(result)
print('----------------------------------')
fil = [x > 5 or x % 2 == 0 for x in arr]
result = arr[fil]
print(result)
print('----------------------------------')
fil = [x % 2 == 0 for x in arr]
result = arr[fil]
print(result)
print('----------------------------------')
fil = arr % 6 == 0
result = arr[fil]
print(result)
print('----------------------------------')
