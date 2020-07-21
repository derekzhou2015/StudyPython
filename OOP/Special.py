#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__  = 'Kerwin'

class Student(object):
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return 'Student object (name:%s)' % self.name

    #__repr__ = __str__

    #def __iter__(self):

print(Student('Kerwin'))
print("----------------------------------")
class Fib(object):
    def __init__(self,n):
        self.a,self.b = 0,1
        self.__n,self.__i = n,1
    
    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b = self.b , self.a + self.b
        if self.__i > self.__n :
            raise StopIteration
        self.__i += 1
        return self.a

    def __getitem__(self,n):
        a,b,i = 1,1,0
        while i < n :
            a,b = b,a+b
            i+=1
        return a

fib = Fib(5)
print(list(fib))
print(fib[4])
print("----------------------------------")
def student_getattr(self,attr):
    if attr == 'age':
        return 0
    else:
        raise AttributeError('<Student object has no attribute %s >.' % attr)
s2 = Student('Kerwin')
Student.__getattr__ = student_getattr
print(s2.name)
print(s2.age)
print("----------------------------------")
Student.__call__ = lambda self: self.name + ':15502169007' 
s3 = Student('Kerwin')
print(callable(s3))
print(s3())
print("----------------------------------")


