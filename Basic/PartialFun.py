#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import random
from functools import partial

n = "10"
r8 = int(n,base=8)
r10 = int(n)
r16 = int(n,base=16)
print(r8,r10,r16)
print("----------------------------------")

int8 = partial(int,base=8)
print(int8(n))
print("----------------------------------")

max2 = partial(max,key = lambda x: round(random() * 100 + x))
l = list(range(10))
print(l,max2(*l))
print("----------------------------------")
