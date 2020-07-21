#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

def firstCharToUpper(s):
    l = [char.upper() if i == 0 else char.lower() for i,char in enumerate(s) ]
    return "".join(l)

l = ['adam', 'LISA', 'barT']
m = map(firstCharToUpper,l)
print(list(m))
print("----------------------------------")
def prod(l):
    r = reduce(lambda x,y: x*y,l)
    return r
l = [3,5,7,9]
print('3 * 5 * 7 * 9 =', prod(l))
if prod(l) == 945:
    print('测试成功!')
else:
    print('测试失败!')
print("----------------------------------")

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}
def strToFloat(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch],s)
    point = 0
    def to_float(f,n):
        nonlocal point
        if n == -1 :
            point = 1
            return f
        if point == 0 :
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point

    return reduce(to_float,nums,0.0)


print(strToFloat('0'))
print(strToFloat('123.456'))
print(strToFloat('123.45600'))
print(strToFloat('0.1234'))
print(strToFloat('.1234'))
print(strToFloat('120.0034'))
print('strToFloat(\'123.456\') =', strToFloat('123.456'))
if abs(strToFloat('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

print("----------------------------------")

r = reduce(lambda  x,y: x + y,list(range(20)),1)
print(r)
print("----------------------------------")