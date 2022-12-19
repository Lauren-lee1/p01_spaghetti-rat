'''
spaghetti rat: Lauren Lee, Brianna Tieu, Emerson Gelobter, Nada Hameed
SoftDev
p01
'''

import sqlite3
from datetime import datetime
import db

def send_message(user, reciever, message):
    DB_FILE="messaging.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    date = datetime.now()
    check_exist = c.execute("SELECT user FROM messaging WHERE user =? AND reciever=?", (user,reciever)).fetchone()
    if check_exist is None:
        c.execute('INSERT INTO messaging(user,latest_message, date, reciever) VALUES (?,?,?,?)',(user, message, date, reciever))
        table = c.execute("SELECT * from messaging")
        return(table.fetchall())
    else: 
        c.execute('REPLACE INTO messaging(user,latest_message, date, reciever) VALUES (?,?,?,?)',(user, message, date, reciever))
        table = c.execute("SELECT * from messaging")
        return(table.fetchall())

def get_message(user, reciever):
    DB_FILE="messaging.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    return c.execute("SELECT latest_message FROM messaging WHERE user =? AND reciever=?", (user,reciever)).fetchall()

def get_time(user, reciever):
    DB_FILE="messaging.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    return c.execute("SELECT date FROM messaging WHERE user =? AND reciever=?", (user,reciever)).fetchall()