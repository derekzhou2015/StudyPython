#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
from turtle import *
from random import random
from sys import argv

print(argv)


def rndColor():
    return (random(), random(), random())


def drawRect():
    pencolor(rndColor())
    width(4)
    forward(300)

    pencolor(rndColor())
    right(90)
    forward(200)

    pencolor(rndColor())
    right(90)
    forward(300)

    pencolor(rndColor())
    right(90)
    forward(200)
    done()


print("----------------------------------")


def drawStar():
    def begin(x, y):
        pu()
        goto(x, y)
        pd()
        seth(0)
        for i in range(5):
            pencolor(rndColor())
            fd(80)
            rt(144)

    for x in range(-200, 300, 100):
        begin(x, 0)
    done()


print("----------------------------------")

def drawTree():

    colormode(255)

    lt(90)

    lv = 14
    l = 120
    s = 45

    width(lv)

    r = 0
    g = 0
    b = 0
    pencolor(r, g, b)

    penup()
    bk(l)
    pendown()
    fd(l)

    def draw_tree(l, level):
        nonlocal r, g, b
        # save the current pen width
        w = width()

        # narrow the pen width
        width(w * 3.0 / 4.0)
        # set color:
        r = r + 1
        g = g + 2
        b = b + 3
        pencolor(r % 200, g % 200, b % 200)

        l = 3.0 / 4.0 * l

        lt(s)
        fd(l)

        if level < lv:
            draw_tree(l, level + 1)
        bk(l)
        rt(2 * s)
        fd(l)

        if level < lv:
            draw_tree(l, level + 1)
        bk(l)
        lt(s)

        # restore the previous pen width
        width(w)

    speed("fastest")

    draw_tree(l, 4)

    done()
print("----------------------------------")
if __name__ == "__main__":
    if '-rect' in argv:
        drawRect()
    elif '-star' in argv:
        drawStar()
    elif '-tree' in argv:
        drawTree()
