# spaghetti rat: Lauren Lee, Brianna Tieu, Emerson Gelobter, Nada Hameed SoftDev
# P01: ArRESTed Development
# 2022-12-04
# time spent:

#import db
import auth

from flask import Flask, redirect, render_template, request, session, url_for

#====================SQL====================#
'''
db.create_users_db()
db.create_profile_db()
db.create_pref_db()
'''
#===========================================#

#====================FLASK====================#
app = Flask(__name__)

'''
root route, renders the login page
'''
@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    return render_template('login.html')

'''
login route, checks if attempted login matches data in the
database
- if yes --> user goes to home
- if no --> user gets login page with error messages
'''
@app.route("/login", methods =['GET', 'POST'])
def authenticate():
    msg = ""

    user = [request.form['username']]
    passw = [request.form['password']]
    if auth.authLogin(user, passw):
        render_template('home.html', msg = msg)
    
    print("sssssdfsdfdsfsd")
    msg = 'wrong username or password'


    return render_template('login.html', msg=msg)

'''
register route, allows user to create a new account
'''
@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form: # need to check the input to make sure it's valid
            db.add_user(request.form['username'], request.form['password'])
            return render_template('home.html')#, msg = msg)
        else:
            #return error message
            return render_template('register.html')#, msg = msg)
    return render_template('register.html')#, msg = msg)
#================================================#

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
