#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import base64
s = bytes('Kerwin 周', 'utf-8')
print(s)
b64 = base64.b64encode(s)
bstr = base64.b64decode(b64)
print(b64, bstr)
print("----------------------------------")
bs64 = base64.urlsafe_b64encode(s)
bsstr = base64.urlsafe_b64decode(bs64)
print(bs64, bsstr)
print("----------------------------------")
def safe_base64_decode(s):
    if(type(s) != bytes):
        raise TypeError('%s is not bytes.' % s)
    renum = len(s) % 4
    appnum = 4 - renum if renum != 0 else 0
    s = s + b'=' * appnum
    return base64.b64decode(s)

# test:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
print("----------------------------------")
