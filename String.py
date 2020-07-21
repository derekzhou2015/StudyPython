#!/usr/bin/env python3
# -*- coding: utf-8 -*-

str = "周"
asc = ord(str)
char = chr(asc)



enstr = str.encode('utf-8')
destr = enstr.decode('utf-8',errors='ignore')
#print(len(enstr))


str3 = "hellow,%s, nice to meet you. I am  %d old years." % ("kerwin",10)
#print(str3)

str4 = "hellow,{0},nice to meet you. I am {1:.2f} old years".format("Kerwin",10)


print(str4)