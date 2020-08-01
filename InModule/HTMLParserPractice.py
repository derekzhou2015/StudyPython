#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
from html.parser import HTMLParser
from html import unescape, escape

html = '&lt;abc&gt;'
text = unescape(html)
print(text)
html = escape(text)
print(html)
print("----------------------------------")

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self._current_data = ''
        self.images = []
        self.links = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        self._current_data = tag
        if tag == 'a':
            self.links.append(self._get_attr_val(attrs, 'href'))
        if tag == 'section' and self._has_attr_val(attrs, 'title'):
            self._current_data += '.title'

    def handle_endtag(self, tag):
        self._current_data = ''

    def handle_startendtag(self, tag, attrs):
        if tag == 'img':
            self.images.append(self._get_attr_val(attrs, 'src'))

    def handle_data(self, data):
        if self._current_data in ['p', 'span', 'section.title']:
            self.text.append(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

    def _get_attr_val(self, attrs, name='class', val=''):
        l = list(filter(lambda tup: name in tup and val in tup if val !='' else True , attrs))
        val = l[0][1] if len(l) > 0 else ''
        return val

    def _has_attr_val(self, attrs, name='class',val=''):
        return self._get_attr_val(attrs,name,val) != ''


parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"http://www.baidu.com\" target="_blank">html</a> HTML  &nbsp; tutorial...1<br>END</p>
    <img src='images/logo.png' />
    <p>Hello,I'm Kerwin,I'm Chinese.</p>
    <a href='http://www.sina.com'><img src='images/avtar.png' /></a>
    <span>Welcome</span>
    <section class='title'>Part 1 of 3</section>
    <section>Part 2 of 3</section>
</body></html>''')
print('links:',parser.links)
print('images:',parser.images)
print('text:',parser.text)
print("----------------------------------")
