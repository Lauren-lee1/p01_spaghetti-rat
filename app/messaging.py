'''
spaghetti rat: Lauren Lee, Brianna Tieu, Emerson Gelobter, Nada Hameed
SoftDev
p01
'''

import sqlite3
from datetime import datetime
import db
import api

#should be ran on people who chose to take a risk
def random_update_api_db(user, reciever):
    DB_FILE="api.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    response = api.yes_no()

    if response == "yes":
        c.execute('INSERT INTO api(user,other_user,bool) VALUES (?,?)',(user, reciever, 1))
        return True
    else:
        c.execute('INSERT INTO api(user,other_user,bool) VALUES (?,?)',(user, reciever, 0))
        return False

#ran on people that message blindly
def nonrandom_update_api_db(user, reciever):
    DB_FILE="api.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
        
    c.execute('INSERT INTO api(user,other_user,bool) VALUES (?,?)',(user, reciever, 1))

def check_db(user, reciever):
    DB_FILE="api.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    
    bool = c.execute("SELECT bool FROM api WHERE user =? AND reciever=?", (user,reciever)).fetchone()

    if bool is None:
        return False
    else:
        return True
#check if can message
def can_message(user, reciever):
    DB_FILE="api.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    
    bool = c.execute("SELECT bool FROM api WHERE user =? AND reciever=?", (user,reciever)).fetchone()

    if bool == 1:
        return True
    else:
        return False

#should be ran after every message is sent
def update_permission(user, reciever):
    DB_FILE="api.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    message_bool = c.execute("SELECT latest_message FROM messaging WHERE user =? AND reciever=?", (user,reciever)).fetchone()

    DB_FILE="api.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    
    api_bool = c.execute("SELECT bool FROM api WHERE user =? AND reciever=?", (user,reciever)).fetchone()
    
    if api_bool == 0 and message_bool is not None:
         c.execute('REPLACE INTO api(user, reciever, bool) VALUES (?,?,?)',(user, reciever, 1))


#send message
def send_message(user, reciever, message):
    DB_FILE="messaging.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    date = datetime.now()
    bool = c.execute("SELECT bool FROM api WHERE user =? AND reciever=?", (user,reciever)).fetchone()
    if bool == 0:
        return "can't message"
    else: 
         latest = c.execute("SELECT latest_message FROM messaging WHERE user =? AND reciever=?", (user,reciever)).fetchone()
         if latest is None:
            c.execute('INSERT INTO messaging(user, latest_message, date, reciever) VALUES (?,?,?,?)',(user, message, date, reciever))
         else:
            c.execute('REPLACE INTO messaging(user,latest_message, date, reciever) VALUES (?,?,?,?)',(user, message, date, reciever))

#get latest message
def get_message(user, reciever):
    DB_FILE="messaging.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    user_sent = c.execute("SELECT date FROM messaging WHERE user =? AND reciever=?", (user,reciever)).fetchone() ##chamged from fetchall to fetchone
    other_sent = c.execute("SELECT date FROM messaging WHERE user =? AND reciever=?", (reciever, user)).fetchone()##chamged from fetchall to fetchone
   
    user_message = c.execute("SELECT latest_message FROM messaging WHERE user =? AND reciever=?", (user,reciever)).fetchone() ##chamged from fetchall to fetchone
    other_message = c.execute("SELECT latest_message FROM messaging WHERE user =? AND reciever=?", (reciever, user)).fetchone()##chamged from fetchall to fetchone
    if other_sent is not None and user_sent is not None:
        if other_sent > user_sent:
            return str(other_message)
        else:
            return str(user_message)
    if other_sent is None and user_sent is not None:
        return str(user_message))
    if other_sent is not None and user_sent is None:
        return str(other_message)
    if other_sent is None and user_sent is None:
        return ""
    
#get latest message time
def get_time(user, reciever):
    DB_FILE="messaging.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    user_sent = c.execute("SELECT date FROM messaging WHERE user =? AND reciever=?", (user,reciever)).fetchone() ##chamged from fetchall to fetchone
    other_sent = c.execute("SELECT date FROM messaging WHERE user =? AND reciever=?", (reciever, user)).fetchone()##chamged from fetchall to fetchone
   
    if other_sent is not None and user_sent is not None:
        if other_sent > user_sent:
            return str(other_sent)
        else:
            return str(user_sent)
    if other_sent is None and user_sent is not None:
        return str(user_sent)
    if other_sent is not None and user_sent is None:
        return str(other_sent)
    if other_sent is None and user_sent is None:
        return ""

#get latest message user
def get_user(user, reciever):
    DB_FILE="messaging.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    user_sent = c.execute("SELECT date FROM messaging WHERE user =? AND reciever=?", (user,reciever)).fetchone() ##chamged from fetchall to fetchone
    other_sent = c.execute("SELECT date FROM messaging WHERE user =? AND reciever=?", (reciever, user)).fetchone()##chamged from fetchall to fetchone
    
    user_user = c.execute("SELECT user FROM messaging WHERE user =? AND reciever=?", (user,reciever)).fetchone() ##chamged from fetchall to fetchone
    other_user = c.execute("SELECT user FROM messaging WHERE user =? AND reciever=?", (reciever, user)).fetchone()##chamged from fetchall to fetchone
    if other_sent is not None and user_sent is not None:
        if other_sent > user_sent:
            return str(other_user)
        else:
            return str(user_user)
    if other_sent is None and user_sent is not None:
        return str(user_user))
    if other_sent is not None and user_sent is None:
        return str(other_user)
    if other_sent is None and user_sent is None:
        return ""
   