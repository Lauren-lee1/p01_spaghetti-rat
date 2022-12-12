import requests
import json

def love_calculator(name1, name2):
    url = "https://love-calculator.p.rapidapi.com/getPercentage"

    querystring = {"sname":name1,"fname":name2}

    headers = {
        "X-RapidAPI-Key": "7de29e7ccemshe5f10ce923b4d08p19b4c0jsn2e56c233db7a",
        "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return json.loads(response.text)["percentage"]
