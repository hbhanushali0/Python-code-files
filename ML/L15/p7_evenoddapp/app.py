
from flask import Flask, render_template, request


app =  Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/check")
def check():
    num = int(request.args.get("num"))
    res = "even" if num % 2 == 0 else "odd"
    msg = "your number is " + str(num) + " result is " + res
    return render_template("home.html", msg=msg)
    
if __name__ == "__main__":
    app.run(debug = True)




