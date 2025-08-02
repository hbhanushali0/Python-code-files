
from flask import Flask, render_template, request
import pickle


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template("home.html")
    
@app.route("/check", methods = ["GET", "POST"])
def check():
    fs = request.form["fs"]
    r1 = request.form["r1"]
    if r1 == "no":
        fu  = 0
    else:
        fu = 1
    d = [[fs,fu]]
    with open("db.model", "rb") as f:
        model = pickle.load(f)
    
    res = model.predict(d)
    res = str(res)
    return render_template("home.html", msg = res)
    
if __name__ == "__main__":
    app.run(debug = True)
    
    
    
