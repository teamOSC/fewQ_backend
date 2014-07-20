#!/usr/bin/env python

import flask, flask.views
app = flask.Flask(__name__)
from flask import render_template,request
import sqlite3,datetime,requests

class DB:
    conn = sqlite3.connect('data.db',check_same_thread=False)
    c = conn.cursor()     

    def add_to_queue(self,token,name,email,phone,date):
        self.c.execute('''CREATE TABLE IF NOT EXISTS queue
                     (token TEXT,name TEXT,email TEXT,phone TEXT ,date_ TEXT)''')
        self.c.execute("INSERT INTO queue VALUES (?,?,?,?,?)",(token,name,email,phone,date))
        self.conn.commit()

    def exec_query(self,query):
        result_arr = []
        self.c.execute(query)
        try:
            self.c.execute(query)
            for row in self.c:
                result_arr.append(row)
            return result_arr
        except:
            return []

@app.route('/')
def main():
	token = request.args.get('token')
	name = request.args.get('name')
	email = request.args.get('email')
	phone = request.args.get('phone')
	date = datetime.datetime.now().strftime("%d/%m/%Y,%H:%M")
	if not token:
		return "token not found"
	D = DB()
	D.add_to_queue(token,name,email,phone,date)
	return "200"

@app.route('/queue')
def queue():
	D = DB()
	queue_arr = D.exec_query('SELECT * from queue') 
	return render_template('queue.html',queue_arr=queue_arr)

@app.route('/queue/<token>')
def queue2(token):
	D = DB()
	q = "SELECT * from queue where token like '%s'"%token
	arr = D.exec_query(q)
	d = {}
	d['token'] = arr[0][0]
	d['name'] = arr[0][1]
	d['email'] = arr[0][2]
	d['phone'] = arr[0][3]
	return render_template('item.html',item=d)

@app.route('/upload')
def upload():
	token = request.args.get('token')
	email = request.args.get('email')
	order = request.args.get('order')
	payload = { 'token' : token, 'email' : "email",'order' : order}
	r = requests.get("http://tosc.in:8080/transaction", params=payload)
	return str(r.text)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')