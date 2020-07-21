#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__  = 'Kerwin'

class Animal(object):
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def crying(self):
        print('ohohohohohoh....')
    
class Mammal(Animal):
    @property
    def legs(self):
        return self.__legs

    @legs.setter
    def legs(self, value):
        self.__legs = value

class Bird(Animal):
    @property
    def wing(self):
        return self.__wing

    @wing.setter
    def wing(self,value):
        self.__wing = value
    
class RunableMixIn(object):
    def run(self):
        print('Running....')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')


class Dog(Mammal,RunableMixIn):
    def __init__(self, name,legs = 4):
        self.name = name
        self.legs = legs

    def crying(self):
        print('Wang!Wang!Wang!')

class Bat(Mammal,FlyableMixIn):
    def __init__(self, name,legs = 2):
        self.name = name
        self.legs = legs

class Parrot(Bird,FlyableMixIn):
    def __init__(self, name,wing = 2):
        self.name = name
        self.wing = wing

class Ostrich(Bird,RunableMixIn):
    def __init__(self, name,wing = 2):
        self.name = name
        self.wing = wing


def print_animal(animal):
    result = None
    if isinstance(animal,Mammal):
        result = 'I\'m %s,belong to type of mammal, and i have %d legs' % (animal.name,animal.legs)
    else:
        result = 'I\'m %s,belong to type of bird, and i have %d wings' % (animal.name,animal.wing)
    
    print(result)

    if isinstance(animal,RunableMixIn):
        animal.run()
    else:
        animal.fly()

    animal.crying()
    
print_animal(Dog('Dog'))
print("----------------------------------")
print_animal(Bat('Bat',2))
print("----------------------------------")
print_animal(Parrot('Parrot'))
print("----------------------------------")
print_animal(Ostrich('Ostrich'))
print("----------------------------------")
