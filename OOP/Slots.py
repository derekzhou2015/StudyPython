#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__  = 'Kerwin'

from types import MethodType

class Student(object):
    __slots__ = ('print_score','name','age','print_name')

Student.print_score = lambda self: print('Ok')

s = Student()
s.print_score()
print("----------------------------------")
s.print_name = MethodType(lambda self: print('my name is unkwon.'), s)
s.print_name()
print("----------------------------------")

