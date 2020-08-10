#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import sqlite3
import os

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
try:
    #cursor.execute('CREATE TABLE Grades (Id INTEGER PRIMARY KEY AUTOINCREMENT,Grade VARCHAR (20));')
    #cursor.execute("INSERT INTO Grades(Grade)VALUES('二年级')")
    cursor.execute('SELECT * FROM user')
    values = cursor.fetchall()
    print(values)
    conn.commit()
except:
    conn.rollback()
finally:
    cursor.close()
    conn.close()

# -----------------------------------------------------------------------
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
try:
    cursor.execute(
        r"create table user(id varchar(20) primary key,name varchar(20),score int)")
    cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
    cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
    cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
    cursor.execute(r'select id,name,score from user order by score desc')
    values = cursor.fetchall()
    print(f'[ROWS]{values}')
    conn.commit()
except:
    conn.rollback()
finally:
    cursor.close()
    conn.close()


def get_score_in(low, high):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    try:
        cursor.execute(
            'select name from user where score >= ? and score <= ? order by score asc', (low, high))
        values = [item[0] for item in cursor.fetchall()]
        return values
    finally:
        cursor.close()
        conn.close()

# Test:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
os.remove(db_file)