# p01_spaghettiRat

2022-2023 Software Development Project

**spaghetti rat**: Lauren Lee, Brianna Tieu, Emerson Gelobter, Nada Hameed 
SoftDev  
P01: ArRESTed Development  
2022-12-04  
time spent:   

#### Roles:
* **Lauren**: database manipulation, api integration
* **Emerson**: html templates, Flask app
* **Nada**: database manipulation, api integration
* **Brianna**: html templates, Flask app

### Description:
This is a dating app that matches people based on their preferences. Once signed up, users can update their profile with information and preferences. Only the filled out information and a calculation from the love calculator api will be used to determine matches. In order for users to unlock more information of their matches, it is left up to chance by the yes/no api and their answers to riddles by the riddle api. 

### Launch Codes
0. Clone repo

```
git clone git@github.com:Lauren-lee1/p01_spaghettiRat.git
```

1. In the repo, create a venv
```
python -m venv rat
source rat/bin/activate
```

2. Install packages
```
pip install -r requirements.txt
```

3. cd into app directory
```
cd app
```

4. Populate databses

```
python setup.py
```

5. Start Flask server 
```
python __init__.py
```
6. Go to ```http://127.0.0.1:5000/``` in browser
