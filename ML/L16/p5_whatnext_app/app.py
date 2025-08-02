
from flask import Flask, render_template, request
from sqlite3 import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/submit", methods = ["POST"])
def submit():
    na = request.form["na"]
    op = request.form["r1"]
    con = None
    try:
        con = connect("whatnext.db")
        cursor = con.cursor()
        sql = "insert into wn values('%s','%s')"
        cursor.execute(sql % (na,op))
        con.commit()
    except Exception as e:
        con.rollback()
        return render_template("home.html", m = e)
    else:
        msg = "thanks " + str(na) + " "
        return render_template("home.html", m = msg)
    
    
if __name__ == "__main__":
    app.run(debug = True)
    


