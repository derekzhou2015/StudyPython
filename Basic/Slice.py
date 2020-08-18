#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

l = list(range(100))
s = l[0:10]
s = l[10:20]
s = l[:10]
s = l[10:]
s = l[-10:]
s = l[-20:-10]
s = l[:20:3]
s = l[20::3]
s = l[10:20:2]
s = l[:]
name = "my name is Kerwin."
#print(s)
#print(name[3:7])


def trim(s):
    if(len(s) == 0 or (s[0] != " " and s[-1] != " ")):
        return s
    if(len(s) > 0 and s[0] == " "):
        s = s[1:]
    if(len(s) > 0 and s[-1] == " "):
        s = s[:-1]
    return trim(s)
    

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

