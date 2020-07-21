#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l1 = [chr(item) for item in range(65,91)]
print (l1)
print("----------------------------------")
l1 = [chr(item) for item in range(65,91) if item % 2 ==0 ]
print (l1)
print("----------------------------------")
l1 = [chr(item + 1) for item in range(65,91) if item % 2 ==0 ]
print (l1)
print("----------------------------------")
l1 = [chr(item) if item % 2 == 0 else item  for item in range(65,91)]
print (l1)
print("----------------------------------")
l1 = [chr(a) + chr(b) for a in range(65,91) for b in range(97,123)]
print (l1)
print("----------------------------------")
l1 = [chr(a) + chr(a+32) for a in range(65,91)]
print (l1)
print("----------------------------------")
l1 = ['Hello', 'World', 18, 'Apple', None]
l2 = [item.lower() for item in l1 if isinstance(item,str)]
print(l2)
if l2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
print("----------------------------------")