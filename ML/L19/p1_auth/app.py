
from flask import Flask, render_template, request, session, url_for, redirect
from sqlite3 import *


app = Flask(__name__)
app.secret_key = "hbrocks"

@app.route("/")
def home():
    if "username" in session:
        return render_template("home.html", name = session["username"])
    else:
        return redirect(url_for("login"))
        
        
@app.route("/logout", methods = ["GET", "POST"])
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        un = request.form["un"]
        pw = request.form["pw"]
        con = None
        try:
            con = connect("classes.db")
            cursor = con.cursor()
            sql = "select * from users where username = '%s' and password = '%s'"
            cursor.execute(sql % (un,pw))
            data = cursor.fetchall()
            if len(data) == 0:
                return render_template("login.html", msg = "invalid login")
            else:
                session["username"] = un
                return redirect(url_for("home"))
        except Exception as e:
            msg = "issue" + e
            return render_template("signup.html", msg = msg)
            
        finally:
            if con is not None:
                con.close()
    else:
        return render_template("login.html")
        
@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if request.method == "POST":
        un = request.form["un"]
        pw1 = request.form["pw1"]
        pw2 = request.form["pw2"]
        if pw1 == pw2:
            con = None
            try:
                con = connect("classes.db")
                cursor = con.cursor()
                sql = "insert into users values('%s','%s')"
                cursor.execute(sql % (un,pw1))
                con.commit()
                return redirect(url_for("login"))
            except Exception as e:
                con.rollback()
                return render_template("signup.html", msg = "user already registered")
            finally:
                if con is not None:
                    con.close()
                    
        else:
            return render_template("signup.html", msg = "passwords did not match")
    else:
        return render_template("signup.html")
        

if __name__ == "__main__":
    app.run(debug = True)
    
    
