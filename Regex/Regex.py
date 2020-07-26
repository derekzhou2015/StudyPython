#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__  = 'Kerwin'
import re

s = 'kerwin,,,,lee,angla,vikky,,'
l = re.split(r',+',s)
print(l)
print("----------------------------------")
s ='0379 67658635'
m = re.match(r'^(\d{4})\s+(\d*)$',s)
print(m[0],m[1],m[2])
print("----------------------------------")
s = '102300'
g = re.match(r'^(\d+?)(0*)$',s).groups()
print(g)
print("----------------------------------")
re_phone = re.compile(r'^(139|155)\d{8}$')
print(re_phone.search('15502169007'))
print("----------------------------------")


def is_valid_email(addr):
    regex = r'^[A-Za-z0-9\.]+@([A-Za-z_0-9]+\.)+[a-zA-Z]{2,6}$'
    if re.match(regex,addr):
        return True
    else:
        return False

# test:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
print("----------------------------------")

def name_of_email(addr):
    regex =r'^<?([\w\s\d]+)>?[\w\s\d]*@[\w\s\d]+\.[\w\s]+$'
    result = re.match(regex,addr)
    if result:
        return result.group(1)
    else:
        return None

# test:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris','not found. '
assert name_of_email('tom@voyager.org') == 'tom','not found. '
print('ok')
print("----------------------------------")