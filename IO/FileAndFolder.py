#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import os
import stat
print('My computer\'s system is %s.' % os.name.upper())
if hasattr(os,'uname'):
    print(os.uname)
print("----------------------------------")
#print(os.environ)
print("----------------------------------")
#print(os.environ.get('path','default'))
print("----------------------------------")
path = os.path.abspath('.')
path = os.path.join(path,'Resource')
if os.path.exists(path) :
    #os.rmdir(path)
    pass
else:
    os.mkdir(path)
print(path)
t = os.path.split(path)
print(t)
print("----------------------------------")
path = 'info.txt'
print(os.path.splitext(path))
print("----------------------------------")
if not os.path.exists('temp.txt') :
    with open('temp.txt','a',encoding='utf-8') as f :
        f.write('Hello')
else:
    os.rename('temp.txt','itemp.txt')
    os.remove('itemp.txt')
print("----------------------------------")
l = [item for item in os.listdir('.') if os.path.splitext(item)[1] == '.py']
print(l)
print("----------------------------------")
l = [item for item in os.listdir('.') if os.path.isdir(item)]
print(l)
print("----------------------------------")