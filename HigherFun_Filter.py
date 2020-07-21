#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def not_divisible(n):
    def fun1(x):
        return x % n > 0
    return fun1

def primes(max):
    yield 2
    it = odd_iter() 
    i = 0
    while i < max:
        n = next(it) 
        yield n
        it = filter(not_divisible(n), it)
        i = i + 1

print("all of the primes:",list(primes(100)))

print("----------------------------------")

def is_palindrome(n):
    return str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

print("----------------------------------")