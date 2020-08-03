#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
from PIL import Image, ImageFilter, ImageDraw, ImageFont
from random import randint
from collections import namedtuple
img1 = Image.open('images/image1.jpg')
w, h = img1.size
print('Original image size:%d * %d' % (w, h))
img2 = img1.filter(ImageFilter.BLUR)
img2.thumbnail((w/2, h/2))
w, h = img2.size
print('Thumbanil img size:%d * %d' % (w, h))
# img2.save('images/thumb_image2.jpg','jpeg')
# img2.show()
print("----------------------------------")


def rndChar():
    return chr(randint(65, 90))


def rndBackgroundColor():
    return (randint(64, 255), randint(64, 255), randint(64, 255))


def rndFrontColor():
    return (randint(33, 125), randint(33, 125), randint(33, 125))


# 240*60
Size = namedtuple('Size', ['width', 'height'])
size = Size(60 * 4, 60)
img = Image.new('RGB', size, (255, 255, 255))
font = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', 40)
draw = ImageDraw.Draw(img)

for x in range(size.width):
    for y in range(size.height):
        draw.point((x, y), fill=rndBackgroundColor())

for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), fill=rndFrontColor(), font=font,)
img = img.filter(ImageFilter.BLUR)
img.show()
