'''
spaghetti rat: Lauren Lee, Brianna Tieu, Emerson Gelobter, Nada Hameed
SoftDev
p01
'''

#DATABASES

import sqlite3
import datetime
from api import *

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

def get_bad_star_sign(user_star_sign):
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
    if user_star_sign == ["Aquarius"]:
        bad_star_sign = ['Taurus']
    return bad_star_sign

def get_good_star_sign(user_star_sign):
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

def get_good_mbti(mbti):
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

def get_bad_mbti(mbti):
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
    return good_mbti

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

    table = c.execute("SELECT * from pref")
    print("pref table from pref_setup() call")
    print(table.fetchall())

    db.commit() #save changes
    db.close()  #close database

'''
returns how many shared hobbies user and other user have in common
'''
def match_hobbies(user, non_user):
    ret_val = 0
    DB_FILE="profile.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    # check if optional or not
    hobby_1 = c.execute("SELECT hobby_1 FROM profile WHERE user =?", (user,)).fetchone()
    hobby_2 = c.execute("SELECT hobby_2 FROM profile WHERE user =?", (user,)).fetchone()

    other_hobby_1 =  c.execute("SELECT hobby_1 FROM profile WHERE user=?", (other_user)).fetchone()
    other_hobby_2 =  c.execute("SELECT hobby_2 FROM profile WHERE user=?", (other_user)).fetchone()
    if (hobby_2 == other_hobby_2 and hobby_1 == other_hobby_1) or (hobby_1 == other_hobby_2 and hobby_2 == other_hobby_1):
         ret_val = 2
    if  (hobby_2 == other_hobby_2 and hobby_1 != other_hobby_1) or (hobby_2 != other_hobby_2 and hobby_1 == other_hobby_1) or (hobby_1 != other_hobby_2 and hobby_2 == other_hobby_1) or (hobby_1 == other_hobby_2 and hobby_2 != other_hobby_1) :
         ret_val = 1
    return ret_val

'''
returns if other_user star_sign matches other user mbti preferences
'''
def match_star_sign(user, other_user):
    DB_FILE="pref.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    good_star_sign = c.execute("SELECT good_star_sign FROM pref WHERE user =?", (user,)).fetchone()
    bad_star_sign = c.execute("SELECT bad_star_sign FROM pref WHERE user =?", (user,)).fetchone()

    DB_FILE="profile.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    star_sign = c.execute("SELECT star_sign FROM profile WHERE user =?", (other_user,)).fetchone()

    for x in good_star_sign:
        if x == star_sign:
            return 1
    for x in bad_star_sign:
        if x == star_sign:
            return -1
    return 0

'''
returns if other_user mbti matches other user mbti preferences
'''
def match_mbti(user, other_user):
    DB_FILE="pref.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    good_mbti = c.execute("SELECT good_mbti FROM pref WHERE user =?", (user,)).fetchone()
    bad_mbti = c.execute("SELECT bad_mtbi FROM pref WHERE user =?", (user,)).fetchone()

    DB_FILE="profile.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    mbti = c.execute("SELECT mbti FROM profile WHERE user =?", (other_user,)).fetchone()

    for x in good_mbti:
        if x == mbti:
            return 1
    for x in bad_mbti:
        if x == mbti:
            return -1
    return 0

'''
returns if other_user height matches user height preference
'''
def match_height(user, other_user):
    DB_FILE="profile.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    height = c.execute("SELECT heignt FROM profile WHERE user =?", (other_user,)).fetchone()

    DB_FILE="pref.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    low_height = c.execute("SELECT low_heignt FROM pref WHERE user =?", (user,)).fetchone()
    high_height = c.execute("SELECT high_heignt FROM pref WHERE user =?", (user,)).fetchone()

    if height >= low_height and height <= high_height:
        return True
    return False
#===========================need to be tested===================================#
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
def match(user, other_user):
    DB_FILE="profile.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events


    #user preference information:
    use_star_sign = c.execute("SELECT use_star_sign FROM pref WHERE user =?", (user,)).fetchone()
    use_mbti = c.execute("SELECT use_mbti FROM pref WHERE user =?", (user,)).fetchone()

    if use_star_sign == 1:
        good_star_sign = c.execute("SELECT good_star_sign FROM pref WHERE user =?", (user,)).fetchone()
        bad_star_sign = c.execute("SELECT bad_star_sign FROM pref WHERE user =?", (user,)).fetchone()

    if use_mbti == 1 :
        good_mbti = c.execute("SELECT good_mbti FROM pref WHERE user =?", (user,)).fetchone()
        bad_mbti = c.execute("SELECT bad_mbti FROM pref WHERE user =?", (user,)).fetchone()

    low_height = c.execute("SELECT low_height FROM pref WHERE user =?", (user,)).fetchone()
    high_height = c.execute("SELECT high_height FROM pref WHERE user =?", (user,)).fetchone()

    female = c.execute("SELECT female FROM pref WHERE user =?", (user,)).fetchone()
    male = c.execute("SELECT male FROM pref WHERE user =?", (user,)).fetchone()
    nonbinary = c.execute("SELECT nonbinary FROM pref WHERE user =?", (user,)).fetchone()
    gender_pref=[female, male, nonbinary]

    DB_FILE="profile.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    age = c.execute("SELECT age FROM profile WHERE user =?", (user,)).fetchone()
    #hobby_1 = c.execute("SELECT hobby_1 FROM profile WHERE user =?", (user,)).fetchone()
    #hobby_2 = c.execute("SELECT hobby_2 FROM profile WHERE user =?", (user,)).fetchone()
    name = c.execute("SELECT name FROM profile WHERE user =?", (user,)).fetchone()

    #filter by height and gender first:
    female = []
    male = []
    nonbinary = []
    if age > 16:
        if gender_pref[0] == 1:
            female = c.execute("SELECT user FROM profile WHERE age<=? AND age>=? AND gender=?", (age+2, age-2, "female" )).fetchall()
        if gender_pref[1] == 1:
            male = c.execute("SELECT user FROM profile WHERE age<=? AND age>=? AND gender=?", (age+2, age-2, "male" )).fetchall()
        if gender_pref[2] == 1:
            nonbinary = c.execute("SELECT user FROM profile WHERE (age<=? AND age>=?) AND gender=?", (age+2, age-2, "nonbinary" )).fetchall()
    if age <= 16:
        if gender_pref[0] == 1:
            female = c.execute("SELECT user FROM profile WHERE age<=? AND age>=? AND gender=?", (age+1, age-1, "female" )).fetchall()
        if gender_pref[1] == 1:
            male = c.execute("SELECT user FROM profile WHERE age<=? AND age>=? AND gender=?", (age+1, age-1, "male" )).fetchall()
        if gender_pref[2] == 1:
            nonbinary = c.execute("SELECT user FROM profile WHERE (age<=? AND age>=?) AND gender=?", (age+1, age-1, "nonbinary" )).fetchall()
    total = female + male + nonbinary
    matches = {}
    #=======all no optional==============#
    if use_star_sign == 0 and use_mbti == 0 and low_height is None and high_height is None:
        for x in total:
            x = list(x)[0]
            #love calculator = 50%
            other_name = c.execute("SELECT name FROM profile WHERE user=?", (x)).fetchone()
            love_calc = 0.5 * api.love_calculator(name, other_name)
            #hobby
            shared_hobby = 0
            #other_hobby_1 =  c.execute("SELECT hobby_1 FROM profile WHERE user=?", (x)).fetchone()
            #other_hobby_2 =  c.execute("SELECT hobby_2 FROM profile WHERE user=?", (x)).fetchone()
            if match_hobbies(user, x) == 1:
                shared_hobby = shared_hobby + 30
            if match_hobbies(user, x) == 2:
                shared_hobby = shared_hobby + 20
            matches[x] = (shared_hobby + love_calc)
    #============ all optional selected ====================#
    if use_star_sign == 1 and use_mbti == 1 and low_height is not None and high_height is not None:
        for x in total:
            x = list(x)[0]
            #star sign
            star_sign_score = 0
            if match_star_sign(user, x) == 1:
                star_sign_score = 15
            if match_star_sign(user, x) == -1:
                star_sign_score = -10
            #mbti
            mbti_score = 0
            if match_mbti(user, x) == 1:
                mbti_score = 20
            if match_mbti(user, x) == -1:
                mbti_score = -10
            #height
            height_score = 0
            if match_height(user, x):
                height_score = 20
            if match_height(x, user):
                height_score = height_score + 20
            height_score = height_score/2
            #hobby
            shared_hobby = 0
            if match_hobbies(user, x) == 1:
                shared_hobby = 10
            if match_hobbies(user, x) == 2:
                shared_hobby = 25
            #love calculator
            other_name = c.execute("SELECT name FROM profile WHERE user=?", (x)).fetchone()
            love_calc = 0.2 * api.love_calculator(name, other_name)
            #total
            matches[x] = (star_sign_score + mbti_score + height_score + shared_hobby + love_calc)
    #================= any one is optional ======================#
    optional = [15, 20, 20]
    options = [True, True, True]
    if use_star_sign == 0 or use_mbti == 0 or low_height is None and high_height is None:
        if use_star_sign == 0 :
            options[0] = False
        if use_mbti == 0:
            options[1] = False
        if low_height is None:
            options[2] = False
        total_points = 0
        counter = 0
        for x in range(3):
            if options[x] == False:
                counter = counter + 1
                total_points = total_points + optional[x]
        for x in total:
            x = list(x)[0]
            #star sign
            star_sign_score = 0
            if use_star_sign == 1:
                if match_star_sign(user, x) == 1:
                    star_sign_score = 15
                if match_star_sign(user, x) == -1:
                    star_sign_score = -10
            #mbti
            mbti_score = 0
            if use_mbti == 1:
                if match_mbti(user, x) == 1:
                    mbti_score = 20
                if match_mbti(user, x) == -1:
                    mbti_score = -10
            #height
            height_score = 0
            if low_height is not None:
                if match_height(user, x):
                    height_score = 20
                if match_height(x, user):
                    height_score = height_score + 20
                height_score = height_score/2
            #hobby
            shared_hobby = 0
            if match_hobbies(user, x) == 1:
                shared_hobby = 10
            if match_hobbies(user, x) == 2:
                shared_hobby = 25
            #love calculator
            other_name = c.execute("SELECT name FROM profile WHERE user=?", (x)).fetchone()
            #division
            total_points = points #total_points is how many points are coming from the unused metric(s), points is the points you want distributed to each used metric
            points = (total_points / float(5 - counter)) * (5-counter-1)
            love_calc = ((points + api.love_calculator(name, other_name) ) / (points + 100)) * 20
            matches[x] = (star_sign_score + mbti_score + height_score + shared_hobby + love_calc + points)

'''
get preliminary information of match
*string match (match name)
*dict matches
return name and match percentage
'''

def get_match_info(match, matches):
    DB_FILE="profile.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    name = c.execute("SELECT name FROM profile WHERE user=?", (match)).fetchone()
    percentage = matches[match]

    return name + "\nmatch percentage: " + percentage + "%"

'''
get extra information of match
*dict matches
return birthday, star sign, mbti, height, hobbies, and spotify
'''
def get_extra_match_info(match):
    DB_FILE="profile.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    birthday = c.execute("SELECT birthday FROM profile WHERE user=?", (match)).fetchone()
    star_sign = c.execute("SELECT star_sign FROM profile WHERE user=?", (match)).fetchone()
    mbti = c.execute("SELECT mbti FROM profile WHERE user=?", (match)).fetchone()

    height = c.execute("SELECT height FROM profile WHERE user=?", (match)).fetchone()
    hobby_1 = c.execute("SELECT hobby_1 FROM profile WHERE user=?", (match)).fetchone()
    hobby_2 = c.execute("SELECT hobby_2 FROM profile WHERE user=?", (match)).fetchone()

    spotify = c.execute("SELECT spotify FROM profile WHERE user=?", (match)).fetchone()

    return "\nbirthday: " + birthday + "\nstar sign: " + star_sign + "\nmbti: " + mbti + "\nheight: " + height + "\nhobby 1: " + hobby_1 + "\nhobby 2: " + hobby_2

