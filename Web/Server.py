#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'

from wsgiref.simple_server import make_server
from Hello import application

HOST = ''
PORT = 8000
httpd = make_server('', 8000, app=application)
print(f'[SERVER] Serving HTTP on port {PORT}...')
httpd.serve_forever()