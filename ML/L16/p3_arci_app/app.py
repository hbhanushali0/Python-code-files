
from flask import Flask, render_template, request
from math import pi, pow

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/calculate", methods = ["POST"])
def calculate():
    ra = float(request.form["ra"])
    ar = pi * pow(ra, 2)
    ci = 2 * pi * ra
    ar = round(ar,2)
    ci = round(ci, 2)

    msg = "area = " + str(ar) + " circumference = " + str(ci)
    return render_template("home.html", m= msg)
    
if __name__ == "__main__":
    app.run(debug = True)
    


