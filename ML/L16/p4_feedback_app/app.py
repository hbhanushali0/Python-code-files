
from flask import Flask, render_template, request
from sqlite3 import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/submit", methods = ["POST"])
def submit():
    na = request.form["na"]
    fb = request.form["fb"]
    print(na,fb)
    con = None
    try:
        con = connect("feedback.db")
        cursor = con.cursor()
        sql = "insert into fb values('%s','%s')"
        cursor.execute(sql % (na,fb))
        con.commit()
    except Exception as e:
        con.rollback()
        return render_template("home.html", m = e)
    else:
        msg = "thanks " + str(na) + " for your feedback"
        return render_template("home.html", m = msg)
    
    
if __name__ == "__main__":
    app.run(debug = True)
    


