'''
spaghetti rat: Lauren Lee, Brianna Tieu, Emerson Gelobter, Nada Hameed
SoftDev
p01
'''

#DATABASES

import sqlite3
import datetime

'''
creates users table:
user (string) | pass (string)
'''
def create_users_db():
    DB_FILE="users.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create it
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    # users table
    c.execute("CREATE TABLE IF NOT EXISTS users(user TEXT, pass TEXT)")

    db.commit() #save changes
    db.close()  #close database

'''
Adds a user into the user.db file given username and password
*string user
*string password
'''
def add_user(user, passw):
    DB_FILE="users.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    # add newly registered people in
    c.execute("INSERT INTO users (user, pass) VALUES (?,?)", (user, passw))

    #prints users table
    table = c.execute("SELECT * from users")
    print("user table from add_user() call")
    print(table.fetchall())

    db.commit() #save changes
    db.close()  #close database

'''
Used for user.db
Checks if login credentials match any in the database
'''
def valid_login(user, passw):
    DB_FILE="users.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    # check if username is in table
    username = c.execute("SELECT user FROM users WHERE user = ?", (user,)).fetchone()

    if username is None:
        exists = False
    else:
        exists = True

    # check if password is in table
    password = c.execute("SELECT pass FROM users WHERE pass =?", (passw,)).fetchone()
    if password is None:
        exists = False

    db.commit() #save changes
    db.close()  #close database
    return exists

def user_exists(user):
    DB_FILE="users.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    username = c.execute("SELECT user FROM users WHERE user = ?", (user,)).fetchone()

    if username is None:
        exists = False
    else:
        exists = True

    db.commit() #save changes
    db.close()  #close database
    return exists

'''
creates profile table:
user (string) | name (string) |
birthday (string) | star_sign (string) |
height (int) | age (int) |
hobby_1 (string) | hobby_2 (string) |
spotify (string) *optional* | gender (string) | mbti (string)
'''
def create_profile_db():
    DB_FILE="profile.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    # profile table
    c.execute("CREATE TABLE IF NOT EXISTS profile(user TEXT, name TEXT, birthday TEXT, star_sign TEXT, height INTEGER, age INTEGER, hobby_1 TEXT, hobby_2 TEXT, spotify TEXT, gender TEXT, mbti TEXT)")

    db.commit() #save changes
    db.close()  #close database

'''
creates preferences table:
user (string) |
star_sign (string) *optional, for reference* | mbti(string) *optional, for reference* |
use_star_sign (int/boolean) | use_mbti (int/bool) |
low_height (int) *optional*| high_height (int) *optional* |
female (int) *binary* | male (int) *binary* | nonbinary (int) *binary* |
'''
def create_pref_db():
    DB_FILE="pref.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    # preferences table
    c.execute("CREATE TABLE IF NOT EXISTS pref(user TEXT, star_sign TEXT, mbti TEXT, use_star_sign INTEGER, use_mbti INTEGER, low_height INTEGER, high_height INTEGER, female INTEGER, male INTEGER, nonbinary INTEGER)")

    db.commit() #save changes
    db.close()  #close database

'''
creates messaging table:
user (string) |
latest_message (string) |
date (string) |
reciever (string) |
'''
def create_messaging_db():
    DB_FILE="messaging.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    # preferences table
    c.execute("CREATE TABLE IF NOT EXISTS messaging(user TEXT, latest_message TEXT, date TEXT, reciever TEXT)")

    db.commit() #save changes
    db.close()  #close database

#helper functions:
'''
gets year, month, or day given date
* string date
return int
'''
def get_year(date):
    return int(date[0:4])

def get_month(date):
    return int(date[5:7])

def get_date(date):
    return int(date[8:])

'''
calculate star sign
* string birthday
return string star_sign
'''
def set_star_sign(birthday):
    month = get_month(birthday)
    date = get_date(birthday)

    if (month == 3 and date >=21) or (month == 4 and date <=19):
        star_sign = "Aries"
    if (month == 4 and date >=20) or (month == 5 and date <=19):
        star_sign = "Taurus"
    if (month == 5 and date >=21) or (month == 6 and date <=21):
        star_sign = "Gemini"
    if (month == 6 and date >=22) or (month == 7 and date <=22):
        star_sign = "Cancer"
    if (month == 7 and date >=23) or (month == 8 and date <=22):
        star_sign = "Leo"
    if (month == 8 and date >=23) or (month == 9 and date <=22):
        star_sign = "Virgo"
    if (month == 9 and date >=23) or (month == 10 and date <=23):
        star_sign = "Libra"
    if (month == 10 and date >=24) or (month == 11 and date <=21):
        star_sign = "Scorpio"
    if (month == 11 and date >=22) or (month == 12 and date <=21):
        star_sign = "Sagittarius"
    if (month == 12 and date >=22) or (month == 1 and date <=19):
        star_sign = "Capricorn"
    if (month == 1 and date >=20) or (month == 2 and date <=18):
        star_sign = "Aquarius"
    if (month == 2 and date >=19) or (month == 3 and date <=20):
            star_sign = "Pisces"
    return star_sign

def get_bad_star_sign(user_star_sign):
    bad_star_sign = []
    if user_star_sign == 'Aries':
        bad_star_sign = ['Cancer', 'Capricorn']
    if user_star_sign == 'Taurus':
        bad_star_sign = ['Leo', 'Aquarius']
    if user_star_sign == 'Gemini':
        bad_star_sign = ['Virgo', 'Leo']
    if user_star_sign == 'Cancer':
        bad_star_sign = ['Aries', 'Libra']
    if user_star_sign == 'Leo':
        bad_star_sign = ['Taurus', 'Scorpio']
    if user_star_sign == "Virgo":
        bad_star_sign = ['Gemini','Sagittarius']
    if user_star_sign == "Libra":
        bad_star_sign = ['Cancer','Capricorn']
    if user_star_sign == "Scorpio":
        bad_star_sign = ['Gemini','Sagittarius']
    if user_star_sign == "Sagittarius":
        bad_star_sign = ['Virgo','Pisces']
    if user_star_sign == "Capricorn":
        bad_star_sign = ['Aries','Libra']
    if user_star_sign == "Pisces":
        bad_star_sign = ['Gemini','Sagittarius']
    if user_star_sign == "Aquarius":
        bad_star_sign = ['Taurus']
    return bad_star_sign

def get_good_star_sign(user_star_sign):
    good_star_sign = []
    if user_star_sign == 'Aries':
        good_star_sign = ['Gemini', 'Leo', 'Sagittarius', 'Aquarius']
    if user_star_sign == 'Taurus':
        good_star_sign = ['Cancer', 'Virgo', 'Capricorn', 'Pisces']
    if user_star_sign == 'Gemini':
        good_star_sign = ['Aries', 'Leo', 'Libra', 'Aquarius']
    if user_star_sign == 'Cancer':
        good_star_sign = ['Taurus', 'Virgo', 'Scorpio', 'Pisces']
    if user_star_sign == 'Leo':
        good_star_sign = ['Aries', 'Gemini', 'Libra', 'Sagittarius']
    if user_star_sign == "Virgo":
        good_star_sign = ['Taurus','Cancer','Scorpio','Capricorn']
    if user_star_sign == "Libra":
        good_star_sign = ['Gemini','Leo','Sagittarius','Aquarius']
    if user_star_sign == "Scorpio":
        good_star_sign = ['Cancer','Virgo','Pisces','Capricorn']
    if user_star_sign == "Sagittarius":
        good_star_sign = ['Aries','Leo','Libra','Aquarius']
    if user_star_sign == "Capricorn":
        good_star_sign = ['Taurus','Virgo','Scorpio','Pisces']
    if user_star_sign == "Pisces":
        good_star_sign = ['Taurus','Cancer','Scorpio','Capricorn']
    if user_star_sign == "Aquarius":
        good_star_sign = ['Sagittarius','Libra','Gemini','Aries']
    return good_star_sign


'''
calculate age from birthday!
* string birthday
return int age
'''
def set_age(birthday):
    year = get_year(birthday)
    month = get_month(birthday)
    date = get_date(birthday)

    today =str(datetime.date.today())
    today_year = get_year(today)
    today_month = get_month(today)
    today_date = get_date(today)

    age = today_year - year
    if ((month < today_month) or (month == today_month and date < today_date)):
        return age
    else:
        return age-1

def get_good_mbti(user_mbti):
    good_mbti = []
    if user_mbti == "ESTP":
        good_mbti = ['ISTP', 'ESFJ', 'ISFJ']
    if user_mbti == "ISTP":
        good_mbti = ['ESTP', 'ESFJ', 'ISFJ']
    if user_mbti == "ESFP":
        good_mbti = ['ISFP', 'ESTJ', 'ISTJ']
    if user_mbti == "ISFP":
        good_mbti = ['ESFP', 'ESTJ', 'ISTJ']
    if user_mbti == "ESTJ":
        good_mbti = ['ESFP', 'ISFP', 'ISTJ']
    if user_mbti == "ISTJ":
        good_mbti = ['ESFP', 'ISFP', 'ESTJ']
    if user_mbti == "ESFJ":
        good_mbti = ['ESTP','ISTP','ISFJ']
    if user_mbti == "ISFJ":
        good_mbti = ['ESTP','ISTP','ESFJ']
    if user_mbti == "ENFP":
        good_mbti = ['INFP','ENTJ','INTJ']
    if user_mbti == "INFP":
        good_mbti = ['ENFP','ENTJ','INTJ']
    if user_mbti == "ENFJ":
        good_mbti = ['INFJ','ENTP','INTP']
    if user_mbti == "INFJ":
        good_mbti = ['ENFJ','ENTP','INTP']
    if user_mbti == "ENTP":
        good_mbti = ['ENFJ','INFJ','INTP']
    if user_mbti == "INTP":
        good_mbti = ['ENFJ','INFJ','ENTP']
    if user_mbti == "ENTJ":
        good_mbti = ['ENFP','INFP','INTJ']
    if user_mbti == "INTJ":
        good_mbti = ['ENFP','INFP','ENTJ']
    return good_mbti

def get_bad_mbti(user_mbti):
    bad_mbti = []
    if user_mbti == "ESTP":
        bad_mbti = ['ESFP', 'ISFP', 'ENFP', 'INFP']
    if user_mbti == "ISTP":
        bad_mbti = ['ESFP', 'ISFP', 'ENFP', 'INFP']
    if user_mbti == "ESFP":
        bad_mbti = ['ESTP', 'ISTP', 'ENTP', 'INTP']
    if user_mbti == "ISFP":
        bad_mbti = ['ISFP', 'ISTP', 'ENTP', 'INTP']
    if user_mbti == "ESTJ":
        bad_mbti = ['ESFP', 'ISFP', 'ENFP', 'INFJ']
    if user_mbti == "ISTJ":
        bad_mbti = ['ESFP', 'ISFP', 'ENFP', 'INFJ']
    if user_mbti == "ESFJ":
        bad_mbti = ['ESTJ','ISTJ','ENTJ','INTJ']
    if user_mbti == "ISFJ":
        bad_mbti = ['ESTJ','ISTJ','ENTJ','INTJ']
    if user_mbti == "ENFP":
        bad_mbti = ['ESTP','ISTP','ENTP','INTP']
    if user_mbti == "INFP":
        bad_mbti = ['ESTP','ISTP','ENTP','INTP']
    if user_mbti == "ENFJ":
        bad_mbti = ['ESTJ','ISTJ','ENTJ','INTJ']
    if user_mbti == "INFJ":
        bad_mbti = ['ESTJ','ISTJ','ENTJ','INTJ']
    if user_mbti == "ENTP":
        bad_mbti = ['ESFP','ISFP','ENFP','INFP']
    if user_mbti == "INTP":
        bad_mbti = ['ESFP','ISFP','ENFP','INFP']
    if user_mbti == "ENTJ":
        bad_mbti = ['ESFJ','ISFJ','ENFJ','INFJ']
    if user_mbti == "INTJ":
        bad_mbti = ['ESFJ','ISFJ','ENFJ','INFJ']
    return bad_mbti

'''
set up your profile (optional items listed in profile.db setup)
* string users, name, birthday, hobby_1, hobby_2, spotify, gender, mbti
return string "error" if date is incorrect or if non-optional information not filled out
'''
def profile_setup(user, name, birthday, height, hobby_1, hobby_2, spotify, gender, mbti):
    DB_FILE="profile.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    if (name == '' or birthday == '' or height == '' or hobby_1 =='' or hobby_2 =='' or gender == '' or mbti == ''):
        return "error"

    #make birthday useful
    #should be in format xxxx-xx-xx (year, month, date)
    month = get_month(birthday)
    date = get_date(birthday)
    if (month > 12 or month < 1 or date < 1 or date > 31):
        return "error"

    star_sign = set_star_sign(birthday)
    #need to test this
    age = set_age(birthday)
    #mb name space conflict?
    c.execute("INSERT INTO profile (user, name, birthday, star_sign, height, age, hobby_1, hobby_2, spotify, gender, mbti) VALUES (?,?,?,?,?,?,?,?,?,?,?)", (user, name, birthday, star_sign, height, age, hobby_1, hobby_2, spotify, gender, mbti))

    #prints users table
    '''
    table = c.execute("SELECT * from profile")
    print(" table from set up profile call")
    print(table.fetchall())
    '''

    db.commit() #save changes
    db.close()  #close database

'''
updates your profile
* string user, name, birthday, hobby_1, hobby_2, spotify, gender, mbti
'''
def profile_update(user, name, birthday, height, hobby_1, hobby_2, spotify, gender, mbti):
    DB_FILE = "profile.db"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("UPDATE profile SET name = ?, birthday = ?, height = ?, hobby_1 = ?, hobby_2 = ?, spotify = ?, gender = ?, mbti = ? WHERE user = ?", (name, birthday, height, hobby_1, hobby_2, spotify, gender, mbti, user))

    db.commit() #save changes
    db.close() #close database

'''
gets profile / user information
* string user
returns profile information in a list
'''
def get_profile(user):
    DB_FILE = "profile.db"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT name, birthday, height, hobby_1, hobby_2, spotify, gender, mbti FROM profile WHERE user = ?", (user,))
    pro = c.fetchone()

    db.commit() #save changes
    db.close() #close database

    return pro

'''
set up your preference db
'''
def pref_setup(user, star_sign, mbti, use_star_sign, use_mbti, low_height, high_height, female, male, nonbinary):
    DB_FILE="pref.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#you need a gender preference
    if (female is None or male is None or nonbinary is None):
        return 'error'

    c.execute("INSERT INTO pref (user, star_sign, mbti, use_star_sign, use_mbti, low_height, high_height, female, male, nonbinary) VALUES (?,?,?,?,?,?,?,?,?,?)", (user, star_sign, mbti, use_star_sign, use_mbti, low_height, high_height, female, male, nonbinary))

    '''
    table = c.execute("SELECT * from pref")
    print("pref table from pref_setup() call")
    print(table.fetchall())
    '''

    db.commit() #save changes
    db.close()  #close database

'''
updates your preferences
'''
def pref_update(user, star_sign, mbti, use_star_sign, use_mbti, low_height, high_height, female, male, nonbinary):
    DB_FILE = "pref.db"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("UPDATE pref SET star_sign = ?, mbti = ?, use_star_sign = ?, use_mbti = ?, low_height = ?, high_height = ?, female = ?, male = ?, nonbinary = ? WHERE user = ?", (star_sign, mbti, use_star_sign, use_mbti, low_height, high_height, female, male, nonbinary, user))

    db.commit() #save changes
    db.close() #close database

'''
gets preference information
* string user
returns preference information in a list
'''
def get_pref(user):
    DB_FILE = "pref.db"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT star_sign, mbti, use_star_sign, use_mbti, low_height, high_height, female, male, nonbinary FROM pref WHERE user = ?", (user,))
    pref = c.fetchone()

    db.commit() #save changes
    db.close() #close database

    return pref
#===============================================================================
#==================================TESTING======================================
#===============================================================================
''''
create_users_db()
create_profile_db()
create_pref_db()

DB_FILE="profile.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()

print("\n============PROFILE TABLE============\n") #WORKS

profile_setup("grapes", "Nada Hameed", "2005-11-26", "66", "Drawing", "Video Games", "spotify", "female", "INTJ")
profile_setup("hong", "Joshua Hong", "2005-12-30", "70", "Singing", "Dancing", "spotify", "male", "ISFJ")
profile_setup("frog", "Frog Flipper", "2005-07-23", "72", "Video Games", "Dancing", "spotify", "male", "ENFP")

table = c.execute("SELECT * from profile")
print(" table from set up profile call")
print(table.fetchall())

DB_FILE="pref.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()

print("\n============PREF TABLE============\n") #WORKS

pref_setup("grapes", "", "", "1", "1", "68", "74", "0", "1", "0")
pref_setup("hong", "", "", "1", "1", "62", "68", "1", "0", "0")
pref_setup("frog", "", "", "1", "1", "64", "70", "1", "0", "0")

table = c.execute("SELECT * from pref")
print(" table from set up profile call")
print(table.fetchall())

print("\n============MATCH STAR SIGN============\n") #should return -1 ---WORKS
print(match_star_sign("grapes", "hong"))

print("\n============MATCH HEIGHT============\n") #should return true ---WORKS
print(match_height("grapes", "hong"))

print("\n============MATCH HOBBIES============\n") #should return 2 ---WORKS
print(match_hobbies("grapes","hong"))

print("\n============MATCH MBTI============\n") #should return 1 ---WORKS
print(match_mbti("grapes","hong"))

print("\n============MATCH============\n") # --WORKS
print(match("grapes"))
'''