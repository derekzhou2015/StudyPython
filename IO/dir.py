#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
from enum import Enum
import time
import os

CMD = Enum(
    'CMD', ({'cd': 1, 'dir': 1 << 1, 'exit': 1 << 2, 'tree': 1 << 3}))

thead = 'Mode\t\tLastWriteTime\t\t\t\tLenght\tName'
tbody = '{0}\t\t{1}\t\t{2}\t{3}'


def cmd_cd(*args):
    if len(args) < 2 or not os.path.isdir(args[1]):
        raise ValueError('not found this path.')
    os.chdir(args[1])


def cmd_dir(*args):
    print(thead)
    l = [item for item in os.listdir('.')]
    absp = os.path.abspath('.')
    for item in l:
        p = os.path.join(absp, item)
        info = os.stat(p)
        timestr = time.asctime(time.localtime(info.st_mtime))
        print(tbody.format(info.st_mode, timestr, info.st_size, item))

def cmd_tree(*args):
    cur_path = os.path.abspath('.')
    l = [item for item in os.listdir('.')]
    total = []
    for item in l:
        total.append(cur_path + '\\' + item)
        fpath = os.path.join(cur_path,item)
        if os.path.isdir(fpath):
            recur(fpath,total)
    print("----------------------------------")
    for item in total:
        print(item)
    print("----------------------------------")
    print('total:%d' % len(total))
    print("----------------------------------")
def recur(fpath,total):
    l1 = [item for item in os.listdir(fpath)]
    for item in l1:
        total.append(fpath + '\\' + item)
        cur = os.path.join(fpath,item)
        if os.path.isdir(cur):
            recur(cur,total)

def run():
    while True:
        try:
            rec = input('%s>' % os.path.abspath('.')).lower().split(' ')
            if rec[0] == CMD.exit.name:
                exit()
            elif rec[0] == CMD.cd.name:
                cmd_cd(*rec)
            elif rec[0] == CMD.dir.name:
                cmd_dir(*rec)
            elif rec[0] == CMD.tree.name:
                cmd_tree()
        except ValueError as error:
            print(error)


run()
print("----------------------------------")
