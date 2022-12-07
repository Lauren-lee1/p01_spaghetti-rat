'''
spaghetti rat: Lauren Lee, Brianna Tieu, Emerson Gelobter, Nada Hameed
SoftDev
p01
'''

#DATABASES

import sqlite3

def create_users_db():
    DB_FILE="users.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create it
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    # users table
    c.execute("CREATE TABLE IF NOT EXISTS users(user TEXT, password TEXT)")

    db.commit() #save changes
    db.close()  #close database

def create_profile_db():
    DB_FILE="profile.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    # profile table
    c.execute("CREATE TABLE IF NOT EXISTS profile(user TEXT, birthday TEXT, star_sign TEXT, height INTEGER, hobby_1 TEXT, hobby_2 TEXT, spotify TEXT, gender TEXT, mbti TEXT)")

    db.commit() #save changes
    db.close()  #close database

def create_pref_db():
    DB_FILE="pref.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    # preferences table
    c.execute("CREATE TABLE IF NOT EXISTS pref(user TEXT, star_sign TEXT, height_INTEGER, hobby_1 TEXT, hobby_2 TEXT, gender TEXT, bad_star_sign LIST, mbti TEXT, bad_mbti LIST)")

    db.commit() #save changes
    db.close()  #close database

def add_user(user, passw):
    DB_FILE="users.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    # add newly registered people in
    c.execute("INSERT INTO users (name, pw) VALUES (?,?)", (user, passw))

    #prints users table
    table = c.execute("SELECT * from users")
    print("user table from add_user() call")
    print(table.fetchall())

    db.commit() #save changes
    db.close()  #close database

def profile_setup(user, name, birthday, height, hobby_1, hobby_2, spotify, gender, mbti):
    DB_FILE="profile.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    # determine star sign here
    c.execute("INSERT INTO users (user, name, birthday, star_sign, height, hobby_1, hobby_2, spotify, gender, mbti) VALUES (?,?)", (user, passw))

    #prints users table
    table = c.execute("SELECT * from users")
    print("user table from add_user() call")
    print(table.fetchall())

    db.commit() #save changes
    db.close()  #close database
