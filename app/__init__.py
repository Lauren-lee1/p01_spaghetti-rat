# spaghetti rat: Lauren Lee, Brianna Tieu, Emerson Gelobter, Nada Hameed SoftDev
# P01: ArRESTed Development
# 2022-12-04
# time spent:

import db
#import auth

from flask import Flask, redirect, render_template, request, session, url_for

#====================SQL====================#

db.create_users_db()
db.create_profile_db()
db.create_pref_db()

#===========================================#

#====================FLASK====================#
app = Flask(__name__)
app.secret_key = "heightorpersonality"

'''
root route, renders the login page
'''
@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    if 'username' in session: #home page rendered if there is a session
        return render_template('home.html', msg="successfully logged in")
    return render_template('login.html')

'''
login route, checks if attempted login matches data in the
database
- if yes --> user goes to home
- if no --> user gets login page with error messages
'''
@app.route("/login", methods =['GET', 'POST'])
def authenticate():
    user = request.form['username']
    passw = request.form['password']
    #print(db.valid_login(user, passw))

    if db.valid_login(user, passw):
        session['username'] = user
        return render_template('home.html', msg = "successfully logged in")
    else:
        return render_template('login.html', msg="login failed")

'''
register route, allows user to create a new account
'''
@app.route("/register", methods=['GET','POST'])
def register_account():
    if request.method == 'GET':
        return render_template('register.html')
    user = request.form['newUser']
    #user = request.form.get('newUser')
    passw = request.form['newPass']
    #passw = request.form.get('newPass')

    if db.user_exists(user):
        return render_template('register.html', msg="username is in use!")
    else:
        db.add_user(user, passw)
        return render_template('login.html', msg = "user registered!, log in with your new credentials.")

@app.route("/logout", methods=['GET', 'POST'])
def log_out():
    session.pop('username', None)
    return redirect('/')

'''
profile route, allows user to add / edit their personal matching information
'''
#@app.route("/profile", methods=['GET', 'POST'])

#================================================#

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
