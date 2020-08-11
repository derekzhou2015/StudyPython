#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    for k,v in environ.items():
        print(f'{k}\t:{v}')
    body = '<h1>Hello,%s!</h1>' % (environ["PATH_INFO"][1:] or "Web")
    return [body.encode('utf-8')]
