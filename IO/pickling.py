#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import pickle
import json

d = {'name': 'kerwin', 'age': 36, 'gender': 'male'}
b = pickle.dumps(d)
s = pickle.loads(b)
print(b, '\n\r', s)
print("----------------------------------")
with open('person.txt', 'wb') as f:
    pickle.dump(d, f)
with open('person.txt', 'rb',) as f:
    d1 = pickle.load(f)
    print(d1)
print("----------------------------------")
b = json.dumps(d)
s = json.loads(b)
print(b)
print(s)
print("----------------------------------")
with open('person.json', 'w') as f:
    json.dump(d, f)
with open('person.json', 'r',) as f:
    d1 = json.load(f)
    print(d1)
print("----------------------------------")
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s,%s,%s)' % (self.name, self.age, self.score)

s1 = Student('kerwin', 36, 99)
std_data = json.dumps(s1, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)
print("----------------------------------")
rebuild = json.loads(std_data, object_hook=lambda d: Student(
    d['name'], d['age'], d['score']))
print(rebuild)
print("----------------------------------")
obj = dict(name='中文', age=20)
s = json.dumps(obj, ensure_ascii=True)
s1 = json.dumps(obj, ensure_ascii=False)
print(s)
print(s1)
print("----------------------------------")