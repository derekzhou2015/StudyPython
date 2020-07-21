#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__  = 'Kerwin'

class Animal(object):
    
    def run(self):
        print('Animal is running.')
    
class Dog(Animal):
    
    def run(self):
        print('Dog is running.')

class Cat(Animal):
    def run(self):
        print('Cat is running.')

def someone_run(animal):
    if(isinstance(animal,Animal)):
        animal.run()
    else:
        print('%s is not the type of animal.' % animal)

someone_run(Animal())
someone_run(Dog())
someone_run(Cat())
someone_run(str)
print("----------------------------------")
