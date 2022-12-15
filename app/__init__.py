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
profile route, allows user to add / edit their personal matching information and creates corresponding profile in db
'''
@app.route("/profile", methods=['GET', 'POST'])
def disp_profile():
    if request.method == 'GET':
        return render_template('profile.html')
    user = session['username']
    name = request.form['name']
    birthday = request.form['birthday']
    height = request.form['height']
    hobby_1 = request.form['hobby1']
    hobby_2 = request.form['hobby2']
    spotify = None
    gender = request.form['gender']
    mbti = request.form['mbti']
    db.profile_setup(user, name, birthday, height, hobby_1, hobby_2, spotify, gender, mbti)
    return render_template('profile.html', personal_info="Your personal information has been successfully updated!")

'''
preferences route, allows user to add / edit their romantic preferences and creates a table with the info in db
'''
@app.route("/preferences", methods=['GET', 'POST'])
def pref_table():
    user = session['username']
    star_sign = request.form['pref_star']
    mbti = request.form['pref_mbti']
    use_star_sign = request.form['use_star']
    use_mbti = request.form['use_mbti']
    low_height = request.form['low_height']
    high_height = request.form['high_height']
    female = request.form['pref_female']
    male = request.form['pref_male']
    nonbinary = request.form['pref_nonbinary']
    db.pref_setup(user, star_sign, mbti, use_star_sign, use_mbti, low_height, high_height, female, male, nonbinary)
    return render_template('profile.html', pref_info="Your preferences have been successfully updated!")

@app.route("/match", methods=['GET', 'POST'])
def disp_matches():
    matchName = ""
    matchPercent = ""
    
    matchList = db.match(session['username'])
    m = matchList.keys()
    matchName = m[0]
    matchPercent = matchList[0]

    return render_template('match.html', matchName = matchName, matchInfo = matchPercent)
#================================================#

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
