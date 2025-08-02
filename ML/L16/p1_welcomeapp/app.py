from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/show")
def show():
    na = request.args.get("na")
    na = na.title()
    msg = "Welcome " + na
    return render_template("home.html", m= msg)
    
if __name__ == "__main__":
    app.run(debug = True)
    





