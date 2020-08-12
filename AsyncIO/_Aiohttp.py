#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import asyncio
from aiohttp import web

HOST = '127.0.0.1'
PORT = 8000
CONTENT_TYPE = 'text/html'

async def index(request):
    await asyncio.sleep(1)
    return web.Response(body=b'<h1>Index Page</h1>',content_type=CONTENT_TYPE)


async def hello(request):
    await asyncio.sleep(1)
    text = '<h1>Hello,%s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'),content_type=CONTENT_TYPE)


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    app.router.add_route('GET','/hello/{name}',hello)
    srv = await loop.create_server(app.make_handler(),HOST,PORT)
    print('[SERVER_MESSAGE] Server started at %s:%d...' % (HOST,PORT))
    return srv

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()