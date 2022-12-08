# spaghetti rat: Lauren Lee, Brianna Tieu, Emerson Gelobter, Nada Hameed SoftDev
# P01: ArRESTed Development
# 2022-12-04
# time spent:

import db

from flask import Flask, redirect, render_template, request, session, url_for

#====================SQL====================#
db.create_users_db()
db.create_profile_db()
db.create_pref_db()


#===========================================#

#====================FLASK====================#
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    return render_template('login.html')


@app.route("/login", methods =['GET', 'POST'])
def authenticate():
    msg = ""

    passing = [request.form['username']]
    pwd_check = c.execute("SELECT password from users where username = ?", passing)
    try:
        if list(pwd_check)[0][0] == request.form['password']:
            session['username']=request.form['username']
            session['password']=request.form['password']
            return render_template('home.html')  # response to a form submission
        else:
            msg = "problem"

    except:
        msg ="error"


    return render_template('login.html', msg=msg)

'''
@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form: # need to check the input to make sure it's valid
            add_user(request.form['username'], request.form['password'])
            profile_setup(user,name, request.form['birthday'],request.form['height'],request.form['hobby_1'],request.form['hobby_2'],request.form['spotify'],request.form['gender'], request.form['mbti'])
            return render_template('home.html')



        else:
            #return error message
    return render_template(register.html)
#================================================#

'''
if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
