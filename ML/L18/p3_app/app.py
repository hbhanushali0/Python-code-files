
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from random import randrange


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
    
@app.route("/generate", methods = ["POST"])
def generate():
    le = int(request.form["length"])
    em = request.form["em"]
    pw = ""
    text = "abcdefghijklmnopqrstuvwxyz"
    d = "0123456789"
   
    if request.form["uc"]:
        text = text + text.upper()
    if request.form["di"]:
        text = text + d
    for i in range(le):
        pw = pw + text[randrange(len(text))]
    print(pw)
    msg = Message("We have send your password", sender = "flask789@gmail.com", recipients = [em])
    msg.body = "your password is " + pw
    mail.send(msg)
    return render_template("home.html", msg = "check your email for password ")
    
    
    
if __name__ == "__main__":
    app.run(debug = True)
    
    
