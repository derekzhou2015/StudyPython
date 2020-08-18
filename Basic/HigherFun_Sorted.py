#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l = list(range(100))
l2 = sorted(l,reverse=True)
print(l2)
print("----------------------------------")
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
l2 = sorted(L,key=by_name)
print(l2)
print("----------------------------------")
l2 = sorted(L,key=lambda t: t[0])
print(l2)
print("----------------------------------")

def by_grades(t):
    return t[1]
l2 = sorted(L,key=by_grades,reverse=True)
print(l2)

print("----------------------------------")

l2 = sorted(L,key=lambda t: t[1],reverse=True)
print(l2)
print("----------------------------------")