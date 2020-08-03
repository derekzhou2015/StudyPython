#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
from requests import get, post
from time import time
params = {'id': 'kerwin', 't': time()}
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
req = get('http://127.0.0.1:8080/data.json', params, headers=headers)
print(req.status_code)
# print(req.text)
# print(req.content)
print(req.url)
print(req.encoding)
json = req.json()
print(json, type(json))
print("----------------------------------")
req = post('http://127.0.0.1:8080/data.json', json=params, headers=headers)
print(req.url)
print(req.encoding)
print("----------------------------------")
upload_file = {'file': open('images/image1.jpg', 'rb')}
req = post('http://127.0.0.1:8080/data.json',
           files=upload_file, headers=headers)
print(req.status_code)
print(req.headers)
print(req.cookies)
print("----------------------------------")
cs = {'token': '12345', 'status': 'working'}
req = get('http://127.0.0.1:8080/data.json', cookies = cs, headers=headers,timeout = 2.5)
print(req)
print("----------------------------------")