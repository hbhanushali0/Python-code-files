
from flask import Flask, render_template, request
from sqlite3 import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/submit", methods = ["POST"])
def submit():
    na = request.form["na"]
    s1 = request.form["s1"]
    t1 = request.form.get("t1")
    o1 = request.form.get("o1")
    c1 = request.form.get("c1")
    j1 = request.form.get("j1")
    top = " "
    if t1:
        top += " tomato"
    if o1:
        top += " onion"
    if c1:
        top += " cheese"
    if j1:
        top += " jalapeno"
    con = None
    try:
        con = connect("pizzaorder.db")
        cursor = con.cursor()
        sql = "insert into pizza values('%s','%s', '%s')"
        cursor.execute(sql % (na,s1,top))
        con.commit()
    except Exception as e:
        con.rollback()
        return render_template("home.html", m = e)
    else:
        msg = "thanks " + str(na) + " for your order"
        return render_template("home.html", m = msg)
    
    
if __name__ == "__main__":
    app.run(debug = True)
    


