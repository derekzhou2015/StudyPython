#!/usr/bin/env python3
# -*- coding: utf-8 -*-
array = ['Bart', 'Lisa', 'Adam']
for item in array:
    print(item)

list1 = list(range(100))
sum1 = 0
print(list1)

for item in list1:
    sum1 += item
print(sum1)

age = 0
while True:
    age = int(input("Please input your age.\r\n"))
    if age % 2 == 0:
        break
    else:
        continue

    