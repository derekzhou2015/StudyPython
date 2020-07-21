#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__  = 'Kerwin'

class Person(object):
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        self.__age = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self,value):
        self.__gender = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        self.__score = value
    

    def __init__(self,name,age,score,gender='unknow'):
        self.__name = name
        self.__age = age
        self.__score = score
        self.__gender = gender
    
    def printScore(self):
        s = 'name: {0}\r\n'
        s += 'age: {1}\r\n'
        s += 'gender: {2}\r\n'
        s += 'score: {3:.2f}'

        s = s.format(self.name,self.age,self.gender,self.score)
        print(s)


p1 = Person('Kerwin',37,97.5)
p2 = Person('Lee',28,99.5)
p1.printScore()
print("----------------------------------")
p2.printScore()
print("----------------------------------")
