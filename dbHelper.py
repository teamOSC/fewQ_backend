#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

class DB:
    conn = sqlite3.connect('data.db',check_same_thread=False)
    c = conn.cursor()     

    def add_user(self,name,email,phone,date,profile=''):
        self.c.execute('''CREATE TABLE IF NOT EXISTS users
                     (name TEXT,email TEXT,phone TEXT,profile TEXT,date_ TEXT )''')
        self.c.execute("INSERT INTO users VALUES (?,?,?,?,?)",(name,email,phone,date,profile))
        self.conn.commit()

    def add_manufacturer(self,beacon_id,name,details,json,date):
        self.c.execute('''CREATE TABLE IF NOT EXISTS manufacturer
                     (beacon_id TEXT,name TEXT,details TEXT,json TEXT,date_ TEXT)''')
        
        self.c.execute("INSERT INTO manufacturer VALUES (?,?,?,?,?)",(beacon_id,name,details,json,date))
        self.conn.commit()

    def add_transaction(self,user_id,beacon_id,details,date):
        self.c.execute('''CREATE TABLE IF NOT EXISTS transaction_
                     (user_id TEXT,beacon_id TEXT,details TEXT,date_ TEXT)''')
        
        self.c.execute("INSERT INTO transaction_ VALUES (?,?,?,?)",(user_id,beacon_id,details,date))
        self.conn.commit()

    def add_feedback(self,user_id,beacon_id,rating,comments):
        self.c.execute('''CREATE TABLE IF NOT EXISTS feedback
                     (user_id TEXT,beacon_id TEXT,rating TEXT,comments TEXT)''')
        
        self.c.execute("INSERT INTO feedback VALUES (?,?,?,?)",(user_id,beacon_id,rating,comments))
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

def test():
    D = DB()
    D.add_user("saurav","stomatrix@gmail.com",'9999999999999','123123')
    D.add_manufacturer("1231c2312","Reebok",'Shoes store','{'':''}','12/34/20114')
    D.add_transaction("saurav23123","c1231c2312",'12/34/2014')
    D.add_feedback('user_id','beacon_id','5','very nice app')

if __name__ == '__main__':
    test()

