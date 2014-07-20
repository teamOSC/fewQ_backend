#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask, flask.views
app = flask.Flask(__name__)

from flask import render_template,request,make_response
import json,urllib2,xml,datetime,hashlib,time
from dbHelper import DB,test

client_pc = '192.168.1.10'

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
    date_ = datetime.datetime.now().strftime("%d/%m/%Y,%H:%M")
    D.add_user(name,email,phone,date_,profile)
    
    return "200"

@app.route('/customer_in')
def customer_in():
    email = request.args.get('email') or ''
    beacon_id = request.args.get('beacon_id')
    D = DB()
    date_ = datetime.datetime.now().strftime("%d/%m/%Y,%H:%M")
    D.add_transaction(email,beacon_id,'check_in',date_)
    d = {}

    if email:
        d['token'] = hashlib.md5(email + str(datetime.datetime.now().strftime("%d%m"))).hexdigest()[:6]

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

    d['history'] = []
    d2 = {}
    d2['name'] = 'Pair of watch'
    d2['date'] = '12th December'
    d['history'].append(d2)
    d2 = {}
    d2['name'] = 'Shoes'
    d2['date'] = '1th December'
    d['history'].append(d2)
    d2 = {}
    d2['name'] = 'Gameboy'
    d2['date'] = '21st December'
    d['history'].append(d2)

    return json.dumps(d)

@app.route('/customer_out')
def customer_out():
    email = request.args.get('email')
    beacon_id = request.args.get('beacon_id')
    D = DB()
    date_ = datetime.datetime.now().strftime("%d/%m/%Y,%H:%M")
    D.add_transaction(email,beacon_id,'check_out',date_)
    q = "Select * from transaction_ where user_id like '%s' and details like 'order_%%'"%email
    arr = D.exec_query(q)
    return json.dumps(arr)

@app.route('/feedback')
def feedback():
    email = request.args.get('email')
    beacon_id = request.args.get('beacon_id')
    rating = request.args.get('rating') or ''
    comments = request.args.get('comments') or ''
    D = DB()
    D.add_feedback(email,beacon_id,rating,comments)
    return "200"

@app.route('/search')
def search():
    email = request.args.get('email')
    D = DB()
    q = "Select * from users where email like '%s'"%email
    arr = D.exec_query(q)
    d = {}
    d['name'] = arr[0][0]
    d['email'] = arr[0][1]
    d['phone'] = arr[0][2]
    d['profile'] = arr[0][3]

    return json.dumps(d)

@app.route('/transaction')
def transaction():
    email = request.args.get('email')
    order = request.args.get('order')
    #token = request.args.get('token')
    D = DB()
    date_ = datetime.datetime.now().strftime("%d/%m/%Y,%H:%M")
    D.add_transaction(email,'','order_'+order,date_)
    return "200"

if __name__ == '__main__':
    #test()
    app.debug = True
    app.run(host='0.0.0.0')

