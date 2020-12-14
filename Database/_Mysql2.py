#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import pymysql.cursors
import random
DB_INFO = {'host': 'localhost', 'user': 'root',
           'password': '123456', 'db': 'test'}
conn = pymysql.connect(**DB_INFO)
cursor = conn.cursor()
try:
    sql = "drop table if exists user"
    cursor.execute(sql)
    sql = 'create table user(id varchar(20) primary key,name varchar(20),score int)'
    cursor.execute(sql)

    sql = 'insert into user (id,name,score) values (%s,%s,%s)'
    data = [
        ('A-001', 'Kerwin', random.randint(0, 100)),
        ('A-002', 'Lee', random.randint(0, 100)),
        ('A-003', 'Vicky', random.randint(0, 100))
    ]
    cursor.executemany(sql, data)
    print('[ROW_COUNT] %d' % cursor.rowcount)
    sql = 'select id,name,score from user order by score desc'
    cursor.execute(sql)
    values = cursor.fetchall()
    print(f'[ROWS] {values}')
    conn.commit()
except BaseException as error:
    conn.rollback()
    print(error)
finally:
    cursor.close()
    conn.close()
