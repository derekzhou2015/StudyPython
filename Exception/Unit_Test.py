#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import unittest


class Dict(dict):
    def __init__(self, **kw):
        super().__init__(self, **kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score > 100 or self.score < 0:
            raise ValueError('this score is error.')
        if self.score >= 80:
            return 'A'
        if self.score >= 60:
            return 'B'
        return 'C'


class TestDict(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        p = {'name': 'kerwin', 'age': 20, 'gender': 'male', 'score': 98}
        d = Dict(**p)
        self.assertEqual(d.name, 'kerwin')
        self.assertEqual(d.gender, 'male')

    def test_key(self):
        d = Dict()
        d.key = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            print(d['empty'])

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            print(d.empty)


class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()


if __name__ == '__main__':
    unittest.main()
