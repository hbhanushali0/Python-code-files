
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///classes.db"
db = SQLAlchemy(app)

class StudentModel(db.Model):
    rno = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    marks = db.Column(db.Integer)
    
    
    def __init__(self,rno,name,marks):
        self.rno = rno
        self.name = name
        self.marks = marks


@app.route("/")
def home():
        d = StudentModel.query.all()
        return render_template("home.html", data = d)
    
    
@app.route("/create",methods=["POST","GET"])
def create():
    if request.method == "POST":
        rno = int(request.form["r"])
        name = request.form["n"]
        marks = int(request.form["m"])
        try:
            stu = StudentModel(rno,name,marks)
            db.session.add(stu)
            db.session.commit()
            return render_template("create.html", msg = "record inserted")
        
        except Exception as e:
            db.session.rollback()
            return render_template("create.html", msg = "issue" + str(e))
             
    else:
        return render_template("create.html")
        

@app.route("/delstu/<int:id>")
def delstu(id):
       StudentModel.query.filter(StudentModel.rno == id).delete()
       db.session.commit()
       return redirect(url_for("home"))
    
    
if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)
    
    
