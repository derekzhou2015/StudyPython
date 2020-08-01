#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'

from urllib import request, response, parse
import json

with request.urlopen('http://127.0.0.1') as f:
    print(f.status, f.reason)
    for k, v in f.getheaders():
        print(k, v)
    print('data:', str(f.read(), encoding='utf-8'))
print("----------------------------------")
req = request.Request('http://127.0.0.1')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s:%s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
print("----------------------------------")
# Post
print('Login to Weibo.cn...')
email = input('Email:')
password = input('Password:')
login_data = parse.urlencode([
    ('username', email),
    ('password', password),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header(
    'Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s:%s' % (k, v))
    print('Data:',f.read().decode('utf-8'))

print("----------------------------------")
#Handler
#proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'}) 
#proxy_auth_handler = request.ProxyBasicAuthHandler()
#proxy_auth_handler.add_password('realm','host','username','password')
#opener = request.build_opener(proxy_handler,proxy_auth_handler)
#with opener.open('http://www.example.com/login.html') as f:
#    pass
#print("----------------------------------")

def fetch_data(url):
    req = request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    with request.urlopen(req,timeout=3000) as rep:
        return json.loads(rep.read().decode('utf-8'))
# test
url = 'http://127.0.0.1:8080/data.json'
data = fetch_data(url)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')
print("----------------------------------")