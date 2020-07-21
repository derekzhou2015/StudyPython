#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
from io import StringIO,BytesIO
content = 'Hello,everyone.\nI\'m Kerwin.'
with StringIO() as f:
    f.write(content)
    print(f.getvalue())
print("----------------------------------")
with StringIO(content) as f:
    for line in f.readlines():
        print(line.strip())
print("----------------------------------")
buffer = 'Python 非常不错。'
with BytesIO() as s:
    s.write(buffer.encode('utf-8'))
    buffer = s.getvalue()
    print(buffer)
print("----------------------------------")
with BytesIO(buffer) as s :
    print(s.read().decode('utf-8'))
print("----------------------------------")