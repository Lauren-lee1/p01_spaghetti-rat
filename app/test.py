import sqlite3

DB_FILE="profile.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()

table = c.execute("SELECT * from profile")
print(" table from set up profile call")
print(table.fetchall())

DB_FILE="pref.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()

table = c.execute("SELECT * from pref")
print(" table from set up pref call")
print(table.fetchall())