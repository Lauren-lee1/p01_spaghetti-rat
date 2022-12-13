import requests
import json

def love_calculator(name1, name2):

    key = ""
    with open("keys/key_love_calculator.txt", "r") as file:
        key = file.read()

    url = "https://love-calculator.p.rapidapi.com/getPercentage"

    querystring = {"sname":name1,"fname":name2}

    headers = {
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return json.loads(response.text)["percentage"]
