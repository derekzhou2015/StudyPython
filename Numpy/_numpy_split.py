#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
'a test class'
__author__ = 'Kerwin'

# arrary
arr1 = np.array(range(10))
arr = np.array_split(arr1, 2)
print(arr)
print(arr[0])
print(arr[1])
print('-----------------------------------')
# split 2D
arr1 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
arr = np.array_split(arr1, 6)
print(arr)
print('-----------------------------------')
arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [
                10, 11, 12], [13, 14, 15], [16, 17, 18]])
arr = np.array_split(arr1, 3, axis=1)
print(arr)
print('-----------------------------------')
arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [
                10, 11, 12], [13, 14, 15], [16, 17, 18]])
arr = np.hsplit(arr1, 3)
print(arr)
print('-----------------------------------')
arr = np.vsplit(arr1, 3)
print(arr)
print('-----------------------------------')
arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], ndmin=3)
arr = np.dsplit(arr1, 3)
print(arr)
print('-----------------------------------')
