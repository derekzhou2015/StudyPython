#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

#num = int(input("Please input a int number."))
#ptr = "you input number is {0:d} then hex is {1:s}."
#print(ptr.format(num,hex(num)))

def quadratic(a,b,c):
    print(a,b,c)
    _t1 = math.pow(b,2) - 4 * a * c
    if _t1 < 0 :
        return 0,0
    _r1 = (-b + math.sqrt(_t1)) / (2 * a)
    _r2 = (-b - math.sqrt(_t1)) / (2 * a)
    return round(_r1,2),round(_r2,2)

def my_split(d,s):
    result = (int(item) for item in d.split(s))
    return result
    
#_a,_b,_c = my_split(input("please input A,B,C.\r\n"),' ')
#_x1,_x2 = quadratic(_a,_b,_c)
#print(_x1,_x2)

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(name,age):
    result = "your name is {0:s} .\n\ryour age is {1:d} .\n\r"
    print(result.format(name,age))

def f2(name,age,city="luoyang"):
    result = "your name is {0:s} .\n\ryour age is {1:d} .\n\r"
    result += "you are from {2:s}" 
    print(result.format(name,age,city))

def f3(name,age,*args):
    result = "your name is {0:s} .\n\ryour age is {1:d} .\n\r"
    result += "your grades are {2:s}" 
    print(result.format(name,age,str(args)))

def f4(name,age,**kw):
    result = "your name is {0:s} .\n\ryour age is {1:d} .\n\r"
    if "city" in kw:
        result += "you live city %s .\n\r" % kw["city"]
    if "zipcode" in kw:
        result += "you live city's zipcode is %s ." % kw["zipcode"]
    print(result.format(name,age))

def f5(name,age,*,city,zipcode,cls):
    result = "your name is {0:s} .\n\ryour age is {1:d} .\n\r"
    result += "you live city {2:s} .\n\r"
    result += "you live city's zipcode is {3:s} .\n\r"
    result += "you are in {4:s} .\n\r"
    print(result.format(name,age,city,zipcode,cls))

info = {"city":"ly","zipcode":"471000","cls":"class 1 grade 1"}

#f5("kerwin",30,**info)

# n! = n * (n-1)!

def factorial(n):
    if n <= 0 or n == 1 :
        return 1
    return n * factorial(n-1)

print(factorial(5))