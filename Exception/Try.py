#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'

from functools import reduce
import logging


def str2num(s):
    try:
        return int(s)
    except:
        raise ValueError("%s can't covert to type of int." % s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    try:
        r = calc('100+200+45')
        print('100+200+345=%d' % r)
        r = calc('99+88+7.4')
        print('99+88+7.4=%d' % r)
    except ValueError as e:
        print(e)
    else:
        print('no error.')
    finally:
        print('completed')


main()

print("----------------------------------")
