#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from functools import wraps,reduce
from time import time,sleep

def log(func):
    @wraps(func)
    def wrapper(*args,**key):
        print("i call function %s()" % func.__name__)
        return func(*args,**key)
    return wrapper

@log
def now():
    print(datetime.now())

print(now.__name__)
now()
print("----------------------------------")

def log1(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**key):
            print("%s,I'm calling function %s()" % (text,func.__name__))
            return func(*args,**key)
        return wrapper
    return decorator

    
def gettime():
    print(datetime.now())

@log1("Kerwin")
def getdate():
    print(datetime.now())


n1= getdate
n2 = log1("Lee")(gettime)

print(n1.__name__,n2.__name__)
print("----------------------------------")
n1()
print("----------------------------------")
n2()
print("----------------------------------")

def metric(fn):
    @wraps(fn)
    def warpper(*args,**key):
        curTime = time()
        result = fn(*args,**key)
        usedTime = time() - curTime
        print('%s executed in %.00f ms.' % (fn.__name__,usedTime * 1000))
        return result
    return warpper

@metric
def fast(x, y):
    sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)

if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功!')

print("----------------------------------")

def doLog(text = None):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args,**key):
            if(text):
                print(text)
            print('begin call %s.' % fn.__name__)
            r = fn(*args,**key)
            print('end call %s.' % fn.__name__)
            return r
        return wrapper
    return decorator
        
@doLog()
def sum(*l):
    print('list= %s' % list(l))
    return reduce(lambda x,y: x + y,l)

print('sum = %d ' % sum(*range(1,10)))

print("----------------------------------")

@doLog('execute')
def add(n,*l):
    print('before list = %s' % list(l))
    return map(lambda x: x + 2,l)

m = add(2,*range(1,10))
print('after list = %s ' % list(m))

print("----------------------------------")