import requests
from urllib import request
import json
from flask import Flask, render_template

def love_calculator(name1, name2):

    key = ""
    try:
        with open("app/key_love_calculator.txt", "r") as file:
            key = file.read().strip()
    except:
        return(0)

    url = "https://love-calculator.p.rapidapi.com/getPercentage"

    querystring = {"sname":name1,"fname":name2}

    headers = {
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return json.loads(response.text)["percentage"]

def yes_no(): #no keys
    url = "https://yesno.wtf/api"
    open = request.urlopen(url)
   
    dictionary = json.loads(open.read())
    return dictionary['answer']

def duck():
    url = "https://random-d.uk/api/quack"

    open = request.urlopen(url)
   
    dictionary = json.loads(open.read())
   
    img = dictionary['url']

    return img
print(type(duck()))