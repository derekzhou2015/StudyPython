#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__  = 'Kerwin'

class Person(object):
    total = 0

    def __init__(self, name,age):
        self.__name = name
        self.__age = age
        Person.total += 1
    
    def print_total(self):
        print('Total is %d .' % Person.total)

p1 = Person('Kerwin',37)
p1.print_total()
p2 = Person('Lee',29)
p2.print_total()
p3 = Person('Vikee',29)
p3.print_total()
print("----------------------------------")


class Student(object):
    count = 0
    def __init__(self, name):
        self.__name = name
        Student.count += 1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
print("----------------------------------")
