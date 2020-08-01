#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import hashlib
import random
s = 'kerwin'
md5 = hashlib.md5(s.encode('utf-8'))
print(md5.hexdigest())
print("----------------------------------")
md5 = hashlib.md5()
md5.update(s.encode('utf-8'))
md5.update(' 37'.encode('utf-8'))
print(md5.hexdigest())
print("----------------------------------")
sha1 = hashlib.sha1()
sha1.update(s.encode('utf-8'))
sha1.update(' 37'.encode('utf-8'))
print(sha1.hexdigest())
print("----------------------------------")

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def calc_md5(password):
    md5 = hashlib.md5(password.encode('utf-8'))
    return md5.hexdigest()


def login(user, password):
    return db[user] == calc_md5(password)


# test:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
print("----------------------------------")

db = {}


def register(username, password):
    try:
        if username in db:
            raise ValueError('error:%s already exists.' % username)
        user = User(username, password)
        db[username] = user
    except ValueError as error:
        print(error)


def get_md5(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()


def user_login(username,password):
    try:
        user = db[username]
        return user.password == get_md5(username + password + user.salt)
    except:
        return False

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(username + password + self.salt)

    def __str__(self):
        return 'username:%s\t\tpasword:%s\tsalt:%s' % (self.username, self.password, self.salt)


register('kerwin', '123456')
register('vicky', '8844332')
register('lee', 'abc123')
register('kerwin', '8844332')

# test:
assert user_login('kerwin', '123456')
assert user_login('vicky', '8844332')
assert user_login('lee', 'abc123')
assert not user_login('kerwin', '1234567')
assert not user_login('vicky', 'a8844332')
assert not user_login('lee', 'abcd123')
print('ok')
print("----------------------------------")
