
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/calculate")
def find():
    num = float(request.args.get("num"))
    res = num * num
    num = round(num,2)
    res = round(res,2)
    msg = "num is " + str(num) + " res is " + str(res)
    return render_template("home.html", msg=msg)

if __name__ == "__main__":
    app.run(debug = True)
    

