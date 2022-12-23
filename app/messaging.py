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
def random_update_api_db(user, other_user):
    DB_FILE="api.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    response = api.yes_no()
    print("response: " + response)
    if response == "yes":
        c.execute('INSERT INTO api(user,other_user,bool) VALUES (?,?,?)',(user, other_user, 1))
        print("yes")
        db.commit() #save changes
        db.close()  #close database
        return True
    else:
        c.execute('INSERT INTO api(user,other_user,bool) VALUES (?,?,?)',(user, other_user, 0))
        print("no")
        db.commit() #save changes
        db.close()  #close database
        return False




#ran on people that message blindly
def nonrandom_update_api_db(user, other_user):
    DB_FILE="api.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
        
    c.execute('INSERT INTO api(user,other_user,bool) VALUES (?,?,?)',(user, other_user, 1))
    table = c.execute("SELECT * from api")
    print(" 22table from set up profile call")
    print(table.fetchall())
    
    db.commit() #save changes
    db.close()  #close database


def check_db(user, other_user):
    DB_FILE="api.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    
    bool = c.execute("SELECT bool FROM api WHERE user =? AND other_user=?", (user,other_user)).fetchone()

    table = c.execute("SELECT * from api")
    print(" -----table from set up profile call")

    db.commit() #save changes
    db.close()  #close database
    #print(table.fetchall())
    if bool is None:
        return False
    else:
        return True
        
    
#check if can message
def can_message(user, other_user):
    DB_FILE="api.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    print("+++++++++++++++++++")
    table = c.execute("SELECT * from api")
    print(" table from set up profile call")
    print(table.fetchall())
    bool = c.execute("SELECT bool FROM api WHERE user =? AND other_user=?", (user,other_user)).fetchone()
    db.commit() #save changes
    db.close()  #close database
    if bool is None:
        return False
    if list(bool)[0] == 1:
        return True
    else:
        return False
        
    # db.commit() #save changes
    # db.close()  #close database
    
#should be ran after every message is sent
def update_permission(user, receiver):
    DB_FILE="messaging.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    message_bool = c.execute("SELECT latest_message FROM messaging WHERE user =? AND receiver=?", (user,receiver)).fetchone()
    db.commit() #save changes
    db.close()  #close database
    DB_FILE="api.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    
    api_bool = c.execute("SELECT bool FROM api WHERE user =? AND other_user=?", (user,receiver)).fetchone()
    db.commit() #save changes
    db.close()  #close database
    if api_bool == 0 and message_bool is not None:
         c.execute('REPLACE INTO api(user, other_user, bool) VALUES (?,?,?)',(user, receiver, 1))


#send message
def send_message(user, receiver, message):
    DB_FILE="api.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    date = datetime.now()
    bool = c.execute("SELECT bool FROM api WHERE user =? AND other_user=?", (user,receiver)).fetchone()
    db.commit() #save changes
    db.close()  #close database

    DB_FILE="messaging.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    if bool == 0:
        return "can't message"
    else: 
         latest = c.execute("SELECT latest_message FROM messaging WHERE user =? AND receiver=?", (user,receiver)).fetchone()
         if latest is None:
            c.execute('INSERT INTO messaging(user, latest_message, date, receiver) VALUES (?,?,?,?)',(user, message, date, receiver))
         else:
            c.execute('REPLACE INTO messaging(user,latest_message, date, receiver) VALUES (?,?,?,?)',(user, message, date, receiver))
    db.commit() #save changes
    db.close()  #close database
    
#get latest message
def get_message(user, receiver):
    DB_FILE="messaging.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    user_sent = c.execute("SELECT date FROM messaging WHERE user =? AND receiver=?", (user,receiver)).fetchone() ##chamged from fetchall to fetchone
    other_sent = c.execute("SELECT date FROM messaging WHERE user =? AND receiver=?", (receiver, user)).fetchone()##chamged from fetchall to fetchone
   
    user_message = c.execute("SELECT latest_message FROM messaging WHERE user =? AND receiver=?", (user,receiver)).fetchone() ##chamged from fetchall to fetchone
    other_message = c.execute("SELECT latest_message FROM messaging WHERE user =? AND receiver=?", (receiver, user)).fetchone()##chamged from fetchall to fetchone
    db.commit() #save changes
    db.close()  #close database
    if other_sent is not None and user_sent is not None:
        if other_sent > user_sent:
            return list(other_message)[0]
        else:
            return list(user_message)[0]
    if other_sent is None and user_sent is not None:
        return list(user_message)[0]
    if other_sent is not None and user_sent is None:
        return list(other_message)[0]
    if other_sent is None and user_sent is None:
        return ""

    
#get latest message time
def get_time(user, receiver):
    DB_FILE="messaging.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    user_sent = c.execute("SELECT date FROM messaging WHERE user =? AND receiver=?", (user,receiver)).fetchone() ##chamged from fetchall to fetchone
    other_sent = c.execute("SELECT date FROM messaging WHERE user =? AND receiver=?", (receiver, user)).fetchone()##chamged from fetchall to fetchone
   
    db.commit() #save changes
    db.close()  #close database

    if other_sent is not None and user_sent is not None:
        if other_sent > user_sent:
            return list(other_sent)[0]
        else:
            return list(user_sent)[0]
    if other_sent is None and user_sent is not None:
        return list(user_sent)[0]
    if other_sent is not None and user_sent is None:
        return list(other_sent)[0]
    if other_sent is None and user_sent is None:
        return ""

#get latest message user
def get_user(user, receiver):
    DB_FILE="messaging.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    user_sent = c.execute("SELECT date FROM messaging WHERE user =? AND receiver=?", (user,receiver)).fetchone() ##chamged from fetchall to fetchone
    other_sent = c.execute("SELECT date FROM messaging WHERE user =? AND receiver=?", (receiver, user)).fetchone()##chamged from fetchall to fetchone
    
    user_user = c.execute("SELECT user FROM messaging WHERE user =? AND receiver=?", (user,receiver)).fetchone() ##chamged from fetchall to fetchone
    other_user = c.execute("SELECT user FROM messaging WHERE user =? AND receiver=?", (receiver, user)).fetchone()##chamged from fetchall to fetchone
    
    db.commit() #save changes
    db.close()  #close database
    
    if other_sent is not None and user_sent is not None:
        if other_sent > user_sent:
            return list(other_user)[0]
        else:
            return list(user_user)[0]
    if other_sent is None and user_sent is not None:
        return list(user_user)[0]
    if other_sent is not None and user_sent is None:
        return list(other_user)[0]
    if other_sent is None and user_sent is None:
        return ""