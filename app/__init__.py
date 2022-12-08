# spaghetti rat: Lauren Lee, Brianna Tieu, Emerson Gelobter, Nada Hameed SoftDev
# P01: ArRESTed Development
# 2022-12-04
# time spent:

import db.py

from flask import Flask, redirect, render_template, request, session, url_for

#====================SQL====================#
create_users_db()


#===========================================#

#====================FLASK====================#
app = Flask(__name__) 

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    
    return render_template( 'login.html')


@app.route("/login", methods =['GET', 'POST'])
def authenticate():
    msg = ""

    passing = [request.form['username']]
    pwd_check = c.execute("SELECT password from users where username = ?", passing)
    try:
        if list(pwd_check)[0][0] == request.form['password']:
            session['username']=request.form['username']
            session['password']=request.form['password']
            userBlogs = list(c.execute("SELECT * from blogs WHERE username = (?)", passing))
            # return redirect(url_for('userpage'))
            return render_template('user.html', user=session['username'], blogList=userBlogs)  # response to a form submission
        else:
            msg = "your password is incorrect"
    except:
        msg = "could not find username in our database"

    return render_template( 'login.html', msg=msg)
        
            
@app.route("/", methods=['GET','POST'])       
def register():
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form: # need to check the input to make sure it's valid
            passing = [request.form['username'], request.form['password']]
            c.execute("INSERT INTO users VALUES (?, ?)", passing) # adds user pass combo into the db
            db.commit()
            return render_template('home.html')

        else:
            
            #error message
    return render_template(register.html)
#================================================#


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
