#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections.abc import Iterable
d = {"name":"Kerwin","age":37,"broncity":"luoyang","zipcode":"471000"}
for key in d:
    print(key)
print("----------------------------------")
for val in d.values():
    print(val)
print("----------------------------------")
for k,v in d.items():
    print(k + ":" + str(v))
print("----------------------------------")
print(isinstance(d,Iterable))
print(isinstance("Kerwin",Iterable))
print(isinstance(123,Iterable))
print("----------------------------------")
for i,(v,k) in enumerate(d.items()):
    print("field_id: %d ,%s : %s" % (i,str(k),str(v)))    
print("----------------------------------")
def findMinAndMax(data):
    result = (None,None) 
    if(len(data) > 0):
        minValue = data[0]
        maxValue = data[0] 
        for item in data:
            if item > maxValue :
                maxValue = item
            if item < minValue :
                minValue = item
        result = (minValue,maxValue)
    return result 
#(minValue,maxValue) = findMinAndMax([-1,3,4,5,6,7,8,199])
#print(minValue,maxValue)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

print("----------------------------------")