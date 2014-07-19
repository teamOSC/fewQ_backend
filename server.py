#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask, flask.views
app = flask.Flask(__name__)

from flask import render_template,request,make_response
import json,urllib2,xml,sqlite3

class DB:
    conn = sqlite3.connect('data.db',check_same_thread=False)
    c = conn.cursor()

    def create_table(self):
        # create new db and make connection
        self.c.execute('''CREATE TABLE IF NOT EXISTS users
                     (name TEXT,email TEXT,phone TEXT,profile TEXT)''')
        self.conn.commit()

    def add_to_db(self,name,email,phone):
        self.create_table()
        self.c.execute("INSERT INTO json VALUES (?,?,?)",(name,email,phone))
        self.conn.commit()

    def return_all(self):
        result_arr = []
        self.c.execute("SELECT * from users")
        for row in self.c:
            result_arr.append(row)
        return result_arr

    def drop_table(self):
        self.create_table()
        self.c.execute("drop table json")
        self.create_table()

@app.route('/foo')
def foo():
    return "foo"

@app.route('/user_register')
def index():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    D = DB()
    D.add_to_db(name,email,phone)
    return "200"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=8080)

