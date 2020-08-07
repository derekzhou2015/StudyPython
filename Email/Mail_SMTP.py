#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr
from smtplib import SMTP

STMP_SERVER = 'smtp.163.com'
STMP_PORT = '25'

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))



from_addr = '******@163.com'
password = '******'
to_addrs = ['******@163.com','******@gmail.com']
# -------------Text--------------------------------
msg = MIMEText('Hello,send by python...', 'plain', 'utf-8')
# -------------HTML----------------------------------
msg = MIMEText('<html><body><h1>Hello</h1>' +
               '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
               '</body></html>', 'html', 'utf-8')
# -------------Attach--------------------------------
msg = MIMEMultipart('alternative')
msg.attach(MIMEText('Hello,send by python...', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><a href="http://www.python.org"><img src="cid:0" /></a></body></html>', 'html', 'utf-8'))

with open('img1.jpg', 'rb') as f:
    mime = MIMEBase('image', 'png', filename='img1.jpg')
    mime.add_header('Content-Disposition', 'attachment', filename='img1.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')

    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

msg['From'] = _format_addr(f'Python fans <{from_addr}>')
msg['To'] = ','.join([_format_addr(f'Manger <{item}>') for item in to_addrs])
msg['Subject'] = Header('From python...', 'utf-8').encode()

server = SMTP(STMP_SERVER, STMP_PORT)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addrs, msg.as_string())
server.quit()
