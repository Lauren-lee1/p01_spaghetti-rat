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
good_star_sign (list) *optional* | height (int) *optional*|
hobby_1 (string) *optional*| hobby_2 (string) *optional*|
gender (string) | bad_star_sign (list) *optional*|
good_mbti (list) *optional*| bad_mbti (list) *optional*|
'''
def create_pref_db():
    DB_FILE="pref.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    # preferences table
    c.execute("CREATE TABLE IF NOT EXISTS pref(user TEXT, good_star_sign LIST, height INTEGER, gender LIST, bad_star_sign LIST, good_mbti TEXT, bad_mbti LIST)")

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
    table = c.execute("SELECT * from profile")
    print(" table from set up profile call")
    print(table.fetchall())

    db.commit() #save changes
    db.close()  #close database

'''
set up your preference db
'''
def pref_setup(user, user_star_sign, height, gender, user_mbti, use_mbti, use_star_sign):
    DB_FILE="pref.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    if user_mbti == False: #no preference set if user doesn't want to use it
        good_mbti == []
        bad_mbti ==[]
    else: #set compatible and incompatible mbti based on mbti
        #https://www.typematchapp.com/16-personalities-compatibility-chart-2/
        if user_mbti == "ESTP":
            good_mbti = ['ISTP', 'ESFJ', 'ISFJ']
            bad_mbti = ['ESFP', 'ISFP', 'ENFP', 'INFP']
        if user_mbti == "ISTP":
            good_mbti = ['ESTP', 'ESFJ', 'ISFJ']
            bad_mbti = ['ESFP', 'ISFP', 'ENFP', 'INFP']
        if user_mbti == "ESFP":
            good_mbti = ['ISFP', 'ESTJ', 'ISTJ']
            bad_mbti = ['ESTP', 'ISTP', 'ENTP', 'INTP']
        if user_mbti == "ISFP":
            good_mbti = ['ESFP', 'ESTJ', 'ISTJ']
            bad_mbti = ['ISFP', 'ISTP', 'ENTP', 'INTP']
        if user_mbti == "ESTJ":
            good_mbti = ['ESFP', 'ISFP', 'ISTJ']
            bad_mbti = ['ESFP', 'ISFP', 'ENFP', 'INFJ']
        if user_mbti == "ISTJ":
            good_mbti = ['ESFP', 'ISFP', 'ESTJ']
            bad_mbti = ['ESFP', 'ISFP', 'ENFP', 'INFJ']
        if user_mbti == "ESFJ":
            good_mbti = ['ESTP','ISTP','ISFJ']
            bad_mbti = ['ESTJ','ISTJ','ENTJ','INTJ']
        if user_mbti == "ISFJ":
            good_mbti = ['ESTP','ISTP','ESFJ']
            bad_mbti = ['ESTJ','ISTJ','ENTJ','INTJ']
        if user_mbti == "ENFP":
            good_mbti = ['INFP','ENTJ','INTJ']
            bad_mbti = ['ESTP','ISTP','ENTP','INTP']
        if user_mbti == "INFP":
            good_mbti = ['ENFP','ENTJ','INTJ']
            bad_mbti = ['ESTP','ISTP','ENTP','INTP']
        if user_mbti == "ENFJ":
            good_mbti = ['INFJ','ENTP','INTP']
            bad_mbti = ['ESTJ','ISTJ','ENTJ','INTJ']
        if user_mbti == "INFJ":
            good_mbti = ['ENFJ','ENTP','INTP']
            bad_mbti = ['ESTJ','ISTJ','ENTJ','INTJ']
        if user_mbti == "ENTP":
            good_mbti = ['ENFJ','INFJ','INTP']
            bad_mbti = ['ESFP','ISFP','ENFP','INFP']
        if user_mbti == "INTP":
            good_mbti = ['ENFJ','INFJ','ENTP']
            bad_mbti = ['ESFP','ISFP','ENFP','INFP']
        if user_mbti == "ENTJ":
            good_mbti = ['ENFP','INFP','INTJ']
            bad_mbti = ['ESFJ','ISFJ','ENFJ','INFJ']
        if user_mbti == "INTJ":
            good_mbti = ['ENFP','INFP','ENTJ']
            bad_mbti = ['ESFJ','ISFJ','ENFJ','INFJ']

#is star sign a factor in determining if you're a match
    if use_star_sign == False:
        good_star_sign == []
        bad_star_sign == []
    else:
        if user_star_sign == 'Aries':
            good_star_sign = ['Gemini', 'Leo', 'Sagittarius', 'Aquarius']
            bad_star_sign = ['Cancer', 'Capricorn']
        if user_star_sign == 'Taurus':
            good_star_sign = ['Cancer', 'Virgo', 'Capricorn', 'Pisces']
            bad_star_sign = ['Leo', 'Aquarius']
        if user_star_sign == 'Gemini':
            good_star_sign = ['Aries', 'Leo', 'Libra', 'Aquarius']
            bad_star_sign = ['Virgo', 'Leo']
        if user_star_sign == 'Cancer':
            good_star_sign = ['Taurus', 'Virgo', 'Scorpio', 'Pisces']
            bad_star_sign = ['Aries', 'Libra']
        if user_star_sign == 'Leo':
            good_star_sign = ['Aries', 'Gemini', 'Libra', 'Sagittarius']
            bad_star_sign = ['Taurus', 'Scorpio']
        if user_star_sign == "Virgo":
            good_star_sign = ['Taurus','Cancer','Scorpio','Capricorn']
            bad_star_sign = ['Gemini','Sagittarius']
        if user_star_sign == "Libra":
            good_star_sign = ['Gemini','Leo','Sagittarius','Aquarius']
            bad_star_sign = ['Cancer','Capricorn']
        if user_star_sign == "Scorpio":
            good_star_sign = ['Cancer','Virgo','Pisces','Capricorn']
            bad_star_sign = ['Gemini','Sagittarius']
        if user_star_sign == "Sagittarius":
            good_star_sign = ['Aries','Leo','Libra','Aquarius']
            bad_star_sign = ['Virgo','Pisces']
        if user_star_sign == "Capricorn":
            good_star_sign = ['Taurus','Virgo','Scorpio','Pisces']
            bad_star_sign = ['Aries','Libra']
        if user_star_sign == "Pisces":
            good_star_sign = ['Taurus','Cancer','Scorpio','Capricorn']
            bad_star_sign = ['Gemini','Sagittarius']

#you need a gender preference
    if (gender == ''):
        return 'error'

    c.execute("INSERT INTO pref (user, good_star_sign, height,  gender, bad_star_sign, good_mbti, bad_mbti) VALUES (?,?,?,?,?,?,?)", (user, good_star_sign, height, hobby_1, hobby_2, gender, bad_star_sign, good_mbti, bad_mbti))

    table = c.execute("SELECT * from pref")
    print("pref table from pref_setup() call")
    print(table.fetchall())

    db.commit() #save changes
    db.close()  #close database

'''
#LOVE API --> uses actual name, not username
def love_pcnt(name, other_name):
    DB_FILE="profile.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    #INTEGRATE API HERE
'''

def match(user, other_user):
    DB_FILE="pref.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    # check if optional or not
'''
matching criteria:
- mbti (optional)
- star sign (optional)
- similar hobbies (at least one hobby is the same)
- gender (female, male, non-binary)
    * yes or no
- age
    * yes or no
    * <= 16 -- one year apart
    * > 16 -- two years apart
- height preferences (optional)
- love calculator (uses first name and the compatibility percentage factors into your match)

don't do optional:
- love calculator (50)
- 1 shared hobby (30)
- 2 shared hobbies (20)

choose all optional:
- Astrology - 15
- MBTI - 20
- Height - 20
- hobby 1 (15)
- hobby 2 (10)
- love calculator (20)

choose 1+ optional:
- remaining percentage is divided up between the number of filled in categories and added
'''
#user preference information:

good_star_sign = c.execute("SELECT good_star_sign FROM pref WHERE user =?", (user,)).fetchone()
bad_star_sign = c.execute("SELECT bad_star_sign FROM pref WHERE user =?", (user,)).fetchone()

good_mbti = c.execute("SELECT good_mbti FROM pref WHERE user =?", (user,)).fetchone()
bad_mbti = c.execute("SELECT bad_mbti FROM pref WHERE user =?", (user,)).fetchone()

height = c.execute("SELECT height FROM pref WHERE user =?", (user,)).fetchone()    

gender = c.execute("SELECT gender FROM pref WHERE user =?", (user,)).fetchone()    

hobby_1 = c.execute("SELECT hobby_1 FROM pref WHERE user =?", (user,)).fetchone()    
hobby_2 = c.execute("SELECT hobby_2 FROM pref WHERE user =?", (user,)).fetchone()    

#height can be list of lowest and greatest inclusive?
if good_star_sign == [] and good_mbti == [] and height == "" and gender ==  "":
    