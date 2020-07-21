#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'

import time
# Read file.
f = open('info.txt', 'r', encoding='utf-8')
print(f.read())
f.close()
print("----------------------------------")
with open('info.txt', 'r', encoding='utf-8') as f:
    print(f.read(6))
print("----------------------------------")
with open('info.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        print('line%d. %s' % (i+1, line.strip()))
print("----------------------------------")
with open('img1.png','rb') as img:
    print(img.read(10))
print("----------------------------------")
with open('info.txt','r',encoding='utf-8',errors='ignore') as f:
    print(f.readline().strip())
    print(f.readline().strip())
print("----------------------------------")
with open('info.txt','a',encoding='utf-8',errors='ignore') as f:
    f.write('I\'m from Henan.%s\n' % time.asctime( time.localtime(time.time())))
print("----------------------------------")
