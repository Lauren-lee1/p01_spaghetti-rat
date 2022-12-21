'''
spaghetti rat: Lauren Lee, Brianna Tieu, Emerson Gelobter, Nada Hameed
SoftDev
p01
'''

import sqlite3
from datetime import datetime
import db
import api

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

    user_sent = c.execute("SELECT latest_message FROM messaging WHERE user =? AND reciever=?", (user,reciever)).fetchone() ##chamged from fetchall to fetchone
    other_sent = c.execute("SELECT latest_message FROM messaging WHERE user =? AND reciever=?", (user,reciever)).fetchone()##chamged from fetchall to fetchone
   
    if other_sent is not None or user_sent is not None:
        if other_sent > user_sent:
            return other_sent
        else:
            return user_sent
    return ""
    

def get_time(user, reciever):
    DB_FILE="messaging.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    return c.execute("SELECT date FROM messaging WHERE user =? AND reciever=?", (user,reciever)).fetchone() ##chamged from fetchall to fetchone

'''
in the case that the user presses the button to see the information
this returns the call of the api and stores it if its no
'''
def ask_api_message(user, other_user):
    DB_FILE="api.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    if api.yes_no() == 'yes':
        return True
    else:
        c.execute('INSERT INTO api(user,other_user) VALUES (?,?)',(user, other_user))
        return False

'''
check if there if the user is in the api db
returns true if user is not in the db so can message
returns false if can't message
'''

def check_api_db(user, other_user):
    DB_FILE="api.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    api_call = c.execute("SELECT user FROM api WHERE user=? AND other_user=?", (user, other_user)).fetchone()
    if api_call is None:
        return True
    else:
        return False
'''
deletes user from db if other user messages them
false -- still cannot edit
true -- can now edit
'''
def allow_message(user, other_user):
    DB_FILE="messaging.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    message = c.execute("SELECT latest_message FROM messaging WHERE user =? AND reciever=?", (other_user,user)).fetchone()
    if message is None:
        return False
    else:
        c.execute('DELETE FROM api(user,other_user) WHERE user=? AND other_user=? (?,?)',(user, other_user))