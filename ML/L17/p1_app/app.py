
from flask import Flask, render_template, request, redirect, url_for
from sqlite3 import *

app = Flask(__name__)

@app.route("/")
def home():
    con  = None
    try:
        
        con = connect("classes.db")
        cursor = con.cursor()
        sql = "select * from student"
        cursor.execute(sql)
        d = cursor.fetchall()
        return render_template("home.html", data = d)
    
    except Exception as e:
        return render_template("home.html", data = "issue" + str(e))
    
    finally:
        if con is not None:
            con.close()
    
@app.route("/create", methods= ["POST", "GET"])
def create():
    if request.method == "POST":
        rno = int(request.form["r"])
        name = request.form["n"]
        marks = int(request.form["m"])
        con = None
        try:
            
            con = connect("classes.db")
            cursor = con.cursor()
            sql = "insert into student values('%d','%s','%d')"
            cursor.execute(sql %(rno, name, marks))
            con.commit()
            return render_template("create.html", msg = "record inserted")
        
        except Exception as e:
            con.rollback()
            return render_template("create.html", msg = "issue" + str(e))
            
        finally:
            if con is not None:
                con.close()
                
    else:
        return render_template("create.html")
        

@app.route("/delstu/<int:id>")
def delstu(id):
    con = None
    try:
        con = connect("classes.db")
        cursor = con.cursor()
        sql = "delete from student where rno = '%d' "
        cursor.execute(sql % (id))
        con.commit()
    except Exception as e:
        con.rollback()
        return render_template("creste.html", msg = "issue" + str(e))
    finally:
        if con is not None:
            con.close()
        return redirect(url_for("home"))
    
    
if __name__ == "__main__":
    app.run(debug = True)
    
    
