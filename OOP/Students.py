#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__  = 'Kerwin'

class Student(object):

    def __init__(self,name,gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self,value):
        l = ['male','female']
        if value in l :
             self.__gender = value
        else:
            raise ValueError('bad gender')


bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
print("----------------------------------")
