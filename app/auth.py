'''
spaghetti rat: Lauren Lee, Brianna Tieu, Emerson Gelobter, Nada Hameed
SoftDev
p01

python file to determine if a login is successful
    - if yes, proceed to the home page
    - if no, return an error message with the login page
'''

import db

from flask import Flask, redirect, render_template, request, session, url_for

#====================SQL====================#

db.create_users_db()
db.create_profile_db()
db.create_pref_db()


def authLogin(user, passw):
    return db.valid_login(user[0], passw[0])
    # msg =""
    
    # print("+++++++++" + passing)
    # pwd_check = c.execute("SELECT password from users where username = ?", passing)
    # try:
    #     if list(pwd_check)[0][0] == passing[0]:
    #         print("true")
    #         return True  # response to a form submission
    #     else:
    #         print("false")
    #         msg = "problem"

    # except:
    #     print("error")
    #     msg ="error"
    # return False

