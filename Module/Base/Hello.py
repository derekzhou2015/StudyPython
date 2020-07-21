#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test module'
__author__  = 'Kerwin'

from sys import argv

def test():
    if len(argv) == 1:
        print("hello,world")
    elif len(argv) ==2 :
        print("hello,world %s" % argv[1])
    else :
        print("too many arguments.")

def _pmethod():
    pass

if __name__ ==' __main__':
    test()