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

    def add_to_db(self,name,email,phone,profile=''):
        self.create_table()
        self.c.execute("INSERT INTO users VALUES (?,?,?,?)",(name,email,phone,profile))
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

@app.route('/user_register',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        name = request.args.get('name')
        email = request.args.get('email')
        phone = request.args.get('phone')
        profile = request.args.get('profile') or ''
    else:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        profile = request.args.get('profile') or ''

    D = DB()
    D.add_to_db(name,email,phone,profile)
    
    return "200"

@app.route('/customer_in')
def customer_in():
    user_id = request.args.get('user_id')
    store_id = request.args.get('store_id')
    d = {}

    d['type'] = 'mall'
    d['items'] = []
    d2 = {}
    d2['title'] = 'Pantaloons'
    d2['text'] = '50%% discount on full sleeves shirts'
    d2['image'] = 'https://joefresh-resource-dev.joefresh.com/JF/b3/WS14WT2290/Dark%20Pink/T.jpg'
    d['items'].append(d2)
    d2 = {}
    d2['title'] = 'Isle 3'
    d2['text'] = '40%% discount on Cheif songs'
    d2['image'] = 'https://joefresh-resource-dev.joefresh.com/JF/b3/KGF4FW9484/Pink/T.jpg'
    d['items'].append(d2)
    d2 = {}
    d2['title'] = 'Books'
    d2['text'] = '20%% discount on Books'
    d2['image'] = 'http://www.llsoft.ca/products/images/BookManager256x256.png'
    d['items'].append(d2)
    d2 = {}
    d2['title'] = 'tops'
    d2['text'] = '10%% discount on tops'
    d2['image'] = 'http://www.wakeeffects.com/shop/images/product/d/dilemma-tank-top-r6679-256px-256px.png'
    d['items'].append(d2)
    return json.dumps(d)

@app.route('/customer_out')
def customer_out():
    user_id = request.args.get('user_id')
    store_id = request.args.get('store_id')
    return ""

def get_user_json(user_id,store_id):
    return ""

def test():
    D =DB()
    D.create_table()
    D.add_to_db("saurav","stomatrix@gmail.com",'9999999999999')

if __name__ == '__main__':
    #test()
    app.debug = True
    app.run(host='0.0.0.0')

