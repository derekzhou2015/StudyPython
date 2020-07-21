#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__  = 'Kerwin'

import Animal as Al
import types

obj = Al.Cat()
print(type(obj))
print(type(obj) == Al.Cat)

print("----------------------------------")

print(type(Al.someone_run) == types.FunctionType)
print(type(Al.someone_run) == types.BuiltinFunctionType)
print(type(lambda : None) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)
print("----------------------------------")

print(isinstance(obj,Al.Cat))
print(isinstance('str',Al.Cat))
print("----------------------------------")
obj.legs = 4
print(dir(obj))
print("----------------------------------")
print(hasattr(obj,'run'))
print("----------------------------------")
print(hasattr(obj,'legs'))
setattr(obj,'legs',3)
print('i have legs %d' % obj.legs)
print("----------------------------------")
fn = getattr(obj,'run')
fn()
print("----------------------------------")