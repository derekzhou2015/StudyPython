#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import chardet
result = chardet.detect(b'Hello,Kerwin.')
print(result)
print("----------------------------------")
data = '仓廪实而知礼节,衣食足而知荣辱'.encode('GBK')
result = chardet.detect(data)
print(result)
print("----------------------------------")
data = '最新の主要ニュース'.encode('euc-jp')
result = chardet.detect(data)
print(result)
print("----------------------------------")
data = '最新の主要ニュース'.encode('utf-8')
encode = chardet.detect(data)
result = data.decode(encode['encoding'])
print(result)
print("----------------------------------")