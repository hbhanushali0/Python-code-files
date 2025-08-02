
from flask import Flask, render_template, request, session, url_for, redirect
from sqlite3 import *
from flask_mail import Mail, Message
from random import randrange


app = Flask(__name__)
app.secret_key = "hbrocks"

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USERNAME"] = "flask6789@gmail.com"
app.config["MAIL_PASSWORD"] = "Flask@123"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False

mail = Mail(app)

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
        con = None
        try:
            con = connect("classes.db")
            cursor = con.cursor()
            pw = ""
            text = "abcdefghijklmnopqrstuvwxyz"
            for i in range(6):
                pw = pw + text[randrange(len(text))]
            sql = "insert into users values('%s','%s')"
            cursor.execute(sql % (un,pw))
            con.commit()
            msg = Message("Welcome to classes", sender = "flask6789@gmail.com", recipients = [un])
            msg.body = "your password is " + pw
            mail.send(msg)
            return redirect(url_for("login"))
        except Exception as e:
            con.rollback()
            return render_template("signup.html", msg = "user already registered" + str(e))
        finally:
            if con is not None:
                con.close()
    else:
        return render_template("signup.html")
        
        
@app.route("/forgotpassword", methods = ["GET","POST"])
def forgotpassword():
    if request.method == "POST":
        un = request.form["un"]
        con = None
        try:
            con = connect("classes.db")
            cursor = con.cursor()
            sql = "select * from users where username = '%s'"
            cursor.execute(sql % (un))
            data = cursor.fetchall()
            if(len(data)) == 0:
                return render_template("fp.html", msg = "user does not exists")
            else:
                pw = ""
                text = "abcdefghijklmnopqrstuvwxyz"
                for i in range(6):
                    pw = pw + text[randrange(len(text))]
                sql = "update users set password = '%s' where username = '%s'"
                cursor.execute(sql % (pw,un))
                con.commit()
                msg = Message("Welcome to Classes", sender = "flask6789@gmail.com", recipients = [un])
                msg.body = "your new password is " + pw
                mail.send(msg)
                return redirect( url_for("login"))
        except Exception as e:
            con.rollback()
            return render_template("signup.html", msg = "user already registered" + str(e))
        finally:
            if con is not None:
                con.close()
    else:
        return render_template("fp.html")
        

if __name__ == "__main__":
    app.run(debug = True)
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    app.run(debug = True)
    
    
