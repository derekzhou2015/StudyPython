#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum, unique
'a test class'
__author__ = 'Kerwin'
Month = Enum('Month', ({'Jan': 1, 'Feb': 1 << 1, 'Mar': 1 << 2, 'Apr': 1 << 3, 'May': 1 << 4, 'Jun': 1 <<
                        5, 'Jul': 1 << 6, 'Aug': 1 << 7, 'Sep': 1 << 8, 'Oct': 1 << 9, 'Nov': 1 << 10, 'Dec': 1 << 11}))


@unique
class Weekday(Enum):
    Sun = 1
    Mon = 1 << 1
    Tue = 1 << 2
    Wed = 1 << 3
    Thu = 1 << 4
    Fri = 1 << 5
    Sat = 1 << 6


print(type(Month))
print(type(Weekday))
print("----------------------------------")
for name, member in Weekday.__members__.items():
    print(name, '=>', member, ',', member.value)
print("----------------------------------")

for member in Month:
    print(member, '=>', member.value)

print("----------------------------------")


@unique
class Gender(Enum):
    Male = 1
    Female = 1 << 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
