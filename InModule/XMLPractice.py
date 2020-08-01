#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'

from xml.parsers.expat import ParserCreate
from urllib import request

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s,attrs:%s' % (name, attrs))

    def end_element(self, name):
        print('sax:end_element:%s' % name)

    def char_data(self, text):
        print('sax:char_data:%s' % text)


handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
print("----------------------------------")
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(r'</root>')
print(''.join(L))
print("----------------------------------")


class WeatherHandler(object):
    def __init__(self):
        self.current_data = ''
        self.city = ''
        self.forecast = []
        self.weather = {}

    def start_element(self, tag, attr):
        self.current_data = tag
        if tag == 'city':
            self.city = attr['name']

    def end_element(self, tag):
        if tag == 'forecast':
            self.forecast.append(self.weather)
            self.weather = {}
        self.current_data = ''

    def char_data(self, text):
        if self.current_data == 'date':
            self.weather['date'] = text
        elif self.current_data == 'high':
            self.weather['high'] = int(text)
        elif self.current_data == 'low':
            self.weather['low'] = int(text)

    def toJSON(self):
        d = {'city': self.city, 'forecast': self.forecast}
        return d


def parseXml(xml_str):
    # print(xml_str)
    parser = ParserCreate(encoding='utf-8')
    handler = WeatherHandler()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    return handler.toJSON()


#test
url = 'http://127.0.0.1:8080/weather.xml'
with request.urlopen(url, timeout=4) as f:
    data = f.read()
result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
print(result,type(result),'ok')
print("----------------------------------")
