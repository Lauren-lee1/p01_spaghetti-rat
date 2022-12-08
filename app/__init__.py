
# spaghetti rat: Lauren Lee, Brianna Tieu, Emerson Gelobter, Nada Hameed SoftDev
# P01: ArRESTed Development
# 2022-12-04
# time spent:

import sqlite3

from flask import Flask, redirect, render_template, request, session, url_for

#====================SQL====================#
#===========================================#

#====================FLASK====================#
app = Flask(__name__) 

@app.route("/", methods=['GET','POST'])       
def login():
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

