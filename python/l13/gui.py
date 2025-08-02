

from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import pymysql
import mysql
 

def f1():
	root.withdraw()
	adst.deiconify()

def f2():
	adst.withdraw()
	root.deiconify()

def f3():
	stViewData.delete(1.0, END)
	root.withdraw()
	vist.deiconify()
	con = None
	try:
		con = pymysql.connect("localhost", "root", "sochosocho", "student")
		cursor = con.cursor()
		sql = "select rno, name from student_thane_jan20"
		cursor.execute(sql)
		data = cursor.fetchall()
		msg = " "
		for d in data:
			msg = msg + "rno = " + str(d[0]) + "name = " + str(d[1]) + "\n"
		stViewData.insert(INSERT, msg)
	
	except Exception as e:
		messagebox.showerror("issue", e)

	finally:
		if con is not None:
			con.close()	
	

def f4():
	vist.withdraw()
	root.deiconify()

def f5():
	con = None
	try:
		con = pymysql.connect("localhost", "root", "sochosocho", "student")
		rno = int(entAddRno.get())
		name = entAddName.get()
		args = (rno, name)
		cursor = con.cursor()
		sql = "insert into student_thane_jan20 values('%d', '%s')"
		cursor.execute(sql % args)
		con.commit()
		messagebox.showinfo("Sahi Kiya", str(cursor.rowcount) + "rows inserted")

	except Exception as e:
		messagebox.showerror("Galat Kiya", e)
		con.rollback()

	finally:
		if con is not None:
			con.close()
		
		entAddRno.delete(0, END)
		entAddName.delete(0, END)
		entAddRno.focus()


root = Tk()
root.title(" S.M.S ")
root.geometry("500x500+300+300")
root.configure(background = "grey")


btnAdd = Button(root, text = "Add", font = ("courier", 18, "bold"), width = 10, command = f1)
btnView = Button(root, text = "View", font = ("courier", 18, "bold"), width = 10, command = f3)
btnAdd.pack(pady = 10)
btnView.pack(pady = 10)


adst = Toplevel(root)
adst.title(" ADD STUDENT")
adst.configure(background = "grey")
adst.geometry("500x500+300+300")
adst.withdraw()


lblAddRno = Label(adst, text = "enter roll no", font = ("courier", 18, "bold"))
entAddRno = Entry(adst, bd = 3.5, font = ("courier", 18, "bold"))
lblAddName = Label(adst, text = "enter name ", font = ("courier", 18, "bold"))
entAddName = Entry(adst, bd = 3.5, font = ("courier", 18, "bold"))
btnAddSave = Button(adst, text = "Save", font = ("courier", 18, "bold"), command = f5)
btnAddBack = Button(adst, text = "Back", font = ("courier", 18, "bold"), command = f2)

lblAddRno.pack(pady = 10)
entAddRno.pack(pady = 10)
lblAddName.pack(pady = 10)
entAddName.pack(pady = 10)
btnAddSave.pack(pady = 10)
btnAddBack.pack(pady = 10)

vist = Toplevel(root)
vist.title(" View St ")
vist.geometry("500x500+300+300")
vist.configure(background = "grey")
vist.withdraw()

stViewData = scrolledtext.ScrolledText(vist, width = 30, height = 10)
btnViewBack = Button(vist, text = "Back", font = ("courier", 18, "bold"), command = f4)
stViewData.pack(pady = 10)
btnViewBack.pack(pady = 10)



root.mainloop()


  