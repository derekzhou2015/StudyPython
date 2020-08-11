#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'

from flask import Flask,request,render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return  render_template('home.html')


@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if (username, password) == ('admin', '123456'):
        return render_template('success.html',username = username)

    return render_template('login.html',message = '[SYSTEM_MESSAGE] Bad username or password.',username = username)


if __name__ == "__main__":
    app.run()
