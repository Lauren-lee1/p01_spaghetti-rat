'''
spaghetti rat: Lauren Lee, Brianna Tieu, Emerson Gelobter, Nada Hameed
SoftDev
p01
'''

#DATABASES

import sqlite3
import datetime
import api
import db

'''
returns how many shared hobbies user and other user have in common
'''
def match_hobbies(user, other_user):
    ret_val = 0
    DB_FILE="profile.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    # check if optional or not
    hobby_1 = c.execute("SELECT hobby_1 FROM profile WHERE user =?", (user,)).fetchone()
    hobby_2 = c.execute("SELECT hobby_2 FROM profile WHERE user =?", (user,)).fetchone()

    other_hobby_1 =  c.execute("SELECT hobby_1 FROM profile WHERE user=?", (other_user,)).fetchone()
    other_hobby_2 =  c.execute("SELECT hobby_2 FROM profile WHERE user=?", (other_user,)).fetchone()
    if (hobby_2 == other_hobby_2 and hobby_1 == other_hobby_1) or (hobby_1 == other_hobby_2 and hobby_2 == other_hobby_1):
         ret_val = 2
    if  (hobby_2 == other_hobby_2 and hobby_1 != other_hobby_1) or (hobby_2 != other_hobby_2 and hobby_1 == other_hobby_1) or (hobby_1 != other_hobby_2 and hobby_2 == other_hobby_1) or (hobby_1 == other_hobby_2 and hobby_2 != other_hobby_1) :
         ret_val = 1
    return ret_val

'''helper fxn for star_sign'''
def get_star_sign(user):
    DB_FILE="profile.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    star_sign = (c.execute("SELECT star_sign FROM profile WHERE user =?", (user,)).fetchone())

    return list(star_sign)[0]

'''
returns if other_user star_sign matches other user mbti preferences
'''
def match_star_sign(user, other_user):
    good_star_sign = db.get_good_star_sign(get_star_sign(user))
    bad_star_sign = db.get_bad_star_sign(get_star_sign(user))

    their_star_sign = get_star_sign(other_user)

    if their_star_sign in good_star_sign:
        return 1
    if their_star_sign in bad_star_sign:
        return -1
    return 0

'''helper fxn for mbti'''
def get_mbti(user):
    DB_FILE="profile.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    mbti = (c.execute("SELECT mbti FROM profile WHERE user =?", (user,)).fetchone())

    return list(mbti)[0]
'''
returns if other_user mbti matches other user mbti preferences
'''
def match_mbti(user, other_user):
    good_mbti = db.get_good_mbti(get_mbti(user))
    bad_mbti = db.get_bad_mbti(get_mbti(user))

    their_mbti = get_mbti(other_user)

    if their_mbti in good_mbti:
        return 1
    if their_mbti in bad_mbti:
        return -1
    return 0

'''
returns if other_user height matches user height preference
'''
def match_height(user, other_user):
    DB_FILE="profile.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    height = c.execute("SELECT height FROM profile WHERE user =?", (other_user,)).fetchone()

    DB_FILE="pref.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    low_height = c.execute("SELECT low_height FROM pref WHERE user =?", (user,)).fetchone()
    high_height = c.execute("SELECT high_height FROM pref WHERE user =?", (user,)).fetchone()

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
def match(user):
    matches = {}
    DB_FILE="pref.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    #matches_sorted = {}

    #user preference information:
    use_star_sign = list(c.execute("SELECT use_star_sign FROM pref WHERE user =?", (user,)).fetchone())[0]
    use_mbti = list(c.execute("SELECT use_mbti FROM pref WHERE user =?", (user,)).fetchone())[0]

    low_height = list(c.execute("SELECT low_height FROM pref WHERE user =?", (user,)).fetchone())[0]
    high_height = list(c.execute("SELECT high_height FROM pref WHERE user =?", (user,)).fetchone())[0]

    female = list(c.execute("SELECT female FROM pref WHERE user =?", (user,)).fetchone())[0]
    male = list(c.execute("SELECT male FROM pref WHERE user =?", (user,)).fetchone())[0]
    nonbinary = list(c.execute("SELECT nonbinary FROM pref WHERE user =?", (user,)).fetchone())[0]
    gender_pref=[female, male, nonbinary]

    DB_FILE="profile.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    age = list(c.execute("SELECT age FROM profile WHERE user =?", (user,)).fetchone())[0]
    #hobby_1 = c.execute("SELECT hobby_1 FROM profile WHERE user =?", (user,)).fetchone()
    #hobby_2 = c.execute("SELECT hobby_2 FROM profile WHERE user =?", (user,)).fetchone()
    name = list(c.execute("SELECT name FROM profile WHERE user =?", (user,)).fetchone())[0]

    #filter by height and gender first:
    total = check_age_gender(user)
    #=======all no optional==============#
    if use_star_sign == 0 and use_mbti == 0 and low_height is None and high_height is None:
        matches = no_optional(user, total)
    #============ all optional selected ====================#
    if use_star_sign == 1 and use_mbti == 1 and low_height is not None and high_height is not None:
         matches = all_optional(user, total)
    #================= any one is optional ======================#
    optional = [15, 20, 20]
    options = [True, True, True]
    if use_star_sign == 0 or use_mbti == 0 or low_height is None and high_height is None:
        ("*******************asdfasdfasd*************")
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
            other_name = c.execute("SELECT name FROM profile WHERE user=?", (x,)).fetchone()
            #division
            points = (total_points / float(5 - counter)) * (5-counter-1)
            total_points = points #total_points is how many points are coming from the unused metric(s), points is the points you want distributed to each used metric
            
            love_calc = ((points + api.love_calculator(name, other_name) ) / (points + 100)) * 20
            matches[x] = (star_sign_score + mbti_score + height_score + shared_hobby + love_calc + points)
    '''   
    for i in sorted(matches.values()):
        key = list(matches)[i]
        value = int(list(matches.values())[i])
        matches_sorted.update({key:float(value)})
    '''
    return check_gender_pref(user, matches)

def check_age_gender(user):
    DB_FILE="pref.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    female = list(c.execute("SELECT female FROM pref WHERE user =?", (user,)).fetchone())[0]
    male = list(c.execute("SELECT male FROM pref WHERE user =?", (user,)).fetchone())[0]
    nonbinary = list(c.execute("SELECT nonbinary FROM pref WHERE user =?", (user,)).fetchone())[0]

    DB_FILE="profile.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    age = list(c.execute("SELECT age FROM profile WHERE user =?", (user,)).fetchone())[0]

    gender_pref=[female, male, nonbinary]
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
    return total

def no_optional(user, total):
    print("*******no optional")
    matches = {}
    DB_FILE="pref.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    use_star_sign = list(c.execute("SELECT use_star_sign FROM pref WHERE user =?", (user,)).fetchone())[0]
    use_mbti = list(c.execute("SELECT use_mbti FROM pref WHERE user =?", (user,)).fetchone())[0]

    low_height = list(c.execute("SELECT low_height FROM pref WHERE user =?", (user,)).fetchone())[0]
    high_height = list(c.execute("SELECT high_height FROM pref WHERE user =?", (user,)).fetchone())[0]

    DB_FILE="profile.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    name = list(c.execute("SELECT name FROM profile WHERE user =?", (user,)).fetchone())[0]

   # if use_star_sign == 0 and use_mbti == 0 and low_height is None and high_height is None:
    for x in total:
        ("**************sssss******************")
        x = list(x)[0]
        #love calculator = 50%
        other_name = c.execute("SELECT name FROM profile WHERE user=?", (x,)).fetchone()
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
    return matches

def all_optional(user, total):
    matches = {}
   # if use_star_sign == 1 and use_mbti == 1 and low_height is not None and high_height is not None:
    print("********************************")
    DB_FILE="profile.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    name = list(c.execute("SELECT name FROM profile WHERE user =?", (user,)).fetchone())[0]
    
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
        other_name = c.execute("SELECT name FROM profile WHERE user=?", (x,)).fetchone()
        love_calc = 0.2 * api.love_calculator(name, other_name)
        #total
        matches[x] = (star_sign_score + mbti_score + height_score + shared_hobby + love_calc)
    return matches

def check_gender_pref(user, matches):
    DB_FILE="profile.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    user_gender = c.execute("SELECT gender FROM profile WHERE user=?", (user, )).fetchone()

    DB_FILE="pref.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    
    if user_gender == "female":
        print("******************female")
        for x in matches:
            if c.execute("SELECT female FROM pref WHERE user=?", (x, )).fetchone() == 0:
                print("&&&&&&&&&&&&&&&&d")
                del matches[x]
    if user_gender == "male":
        print("******************male")
        for x in matches:
            if c.execute("SELECT male FROM pref WHERE user=?", (x, )).fetchone() == 0:
                print("&&&&&&&&&&&&&&&&d")
                del matches[x]
    if user_gender == "nonbinary":
        print("******************nb")
        for x in matches:
            if c.execute("SELECT nonbinary FROM pref WHERE user=?", (x, )).fetchone() == 0:
                print("&&&&&&&&&&&&&&&&d")
                del matches[x]
    return matches
        
    
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

    name = c.execute("SELECT name FROM profile WHERE user=?", (match,)).fetchone()
    percentage = matches[match]

    return [name, percentage]

'''
get extra information of match
*dict matches
return birthday, star sign, mbti, height, hobbies, and spotify
'''
def get_extra_match_info(match):
    DB_FILE="profile.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()

    birthday = c.execute("SELECT birthday FROM profile WHERE user=?", (match,)).fetchone()
    star_sign = c.execute("SELECT star_sign FROM profile WHERE user=?", (match,)).fetchone()
    mbti = c.execute("SELECT mbti FROM profile WHERE user=?", (match,)).fetchone()

    height = c.execute("SELECT height FROM profile WHERE user=?", (match,)).fetchone()
    hobby_1 = c.execute("SELECT hobby_1 FROM profile WHERE user=?", (match,)).fetchone()
    hobby_2 = c.execute("SELECT hobby_2 FROM profile WHERE user=?", (match,)).fetchone()

    spotify = c.execute("SELECT spotify FROM profile WHERE user=?", (match,)).fetchone()

    return [birthday, star_sign, mbti, height, hobby_1, hobby_2]