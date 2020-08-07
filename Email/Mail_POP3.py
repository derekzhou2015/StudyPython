#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'

from poplib import POP3
from email.parser import Parser
from email.utils import parseaddr
from email.header import decode_header

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from io import BytesIO

STMP_SERVER = 'pop.163.com'
USER_ID = '*******'
USER_PWD = '*******'

server = POP3(STMP_SERVER)
server.set_debuglevel(0)
print('[SERVER_MESSAGE] %s' % server.getwelcome().decode('utf-8'))

server.user(USER_ID)
server.pass_(USER_PWD)
print('[SERVER_MESSAGE] Messages:%d,Size:%d' % server.stat())
resp, mails, octets = server.list()

index = len(mails)
resp, lines, octets = server.retr(index)
msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)
server.close()


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header)
            if header == 'Subject':
                value = decode_str(value)
            else:
                hdr, addr = parseaddr(value)
                name = decode_str(hdr)
                value = f'{name} <{addr}>'
            print('%s%s:%s' % ('\t'*indent, header, value))
    if msg.is_multipart():
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('\t' * indent, n))
            print('%s--------------------' % ('\t' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText:%s' % ('\t' * indent,content))
        else:
            content = msg.get_payload(decode=True)
            print('%sAttachment: %s' % ('  ' * indent, content_type))
            f = BytesIO(content)
            img = Image.open(f)
            img.show()
print_info(msg)
