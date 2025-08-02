
from flask import Flask, render_template, request
from datetime import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
    
@app.route("/data")
def submit():
    na = request.args.get("na")
    h = datetime.now().hour
    if h <12:
        m = "Good Morning"
    elif h < 17:
        m = "Good Afternoon"
    else :
        m = "Good Evening"
    
    msg = "Welcome " + str(na) + " " + m
    return render_template("home.html", message=msg)
    
if __name__ == "__main__":
    app.run(debug = True)
    
