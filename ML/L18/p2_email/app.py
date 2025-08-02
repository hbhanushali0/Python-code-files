

from flask import Flask, render_template, request
from sqlite3 import *
from flask_mail import Mail, Message

app = Flask(__name__)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USERNAME"] = "flask789@gmail.com"
app.config["MAIL_PASSWORD"] = "Flask@123"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False

mail = Mail(app)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/subs", methods = ["POST"])
def subs():
    em = request.form["em"]
    if request.form["btn"] == "Subscribe":
        con = None
        try:
            con = connect("email_database.db")
            cursor = con.cursor()
            sql = "select * from users where email = '%s'"
            cursor.execute(sql %(em))
            data = cursor.fetchall()
            if len(data) == 0:
                sql = "insert into users values('%s')"
                cursor.execute(sql % (em))
                con.commit()
                msg = Message("Welcome to the NewsLetter", sender = "flask789@gmail.com", recipients = [em])
                msg.body = "Congrats for your Subscription"
                mail.send(msg)
                return render_template("home.html", msg = "you have been subscribed")
            else:
                return render_template("home.html", msg = "you are already subscribed")
                
        except Exception as e:
            if con is not None:
                con.rollback()
            msg = "issue" + str(e)
            return render_template("home.html", msg = msg)
            
        finally:
            if con is not None:
                con.close()
    elif request.form["btn"] == "Unsubscribe":
        con = None
        try:
            
            con = connect("email_database.db")
            cursor = con.cursor()
            sql = "select * from users where email = '%s'"
            cursor.execute(sql %(em))
            data = cursor.fetchall()
            if len(data) == 1:
                sql = "delete from users where email = '%s'"
                cursor.execute(sql % (em))
                con.commit()
                msg = Message("Msg from Company", sender = "flask789@gmail.com", recipients = [em])
                msg.body = "you have been Successfully Unsubscribed"
                mail.send(msg)
                return render_template("home.html", msg = "you have been un subscribed")
                
            else:
                return render_template("home.html", msg = "you are not Subscribed")
        except Exception as e:
            if con is not None:
                con.rollback()
            msg = "issue" + str(e)
            return render_template("home.html", msg = msg)
            
            
        finally:
            if con is not None:
                con.close()
                
if __name__ == "__main__":
    app.run(debug = True)
    
    
