
# spaghetti rat: Lauren Lee, Brianna Tieu, Emerson Gelobter, Nada Hameed SoftDev
# P01: ArRESTed Development
# 2022-12-04
# time spent:

from flask import Flask
app = Flask(__name__) 

@app.route("/")       
def hello_world():
    return ""

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
