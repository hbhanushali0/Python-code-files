


import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import mysql
import pymysql
import socket

msg = "GREAT TEETH | GREAT SMILE | GREAT LIFE"

def f1():
	root.withdraw()
	adpt.deiconify() 

def f2():
	root.withdraw()
	vdpt.deiconify()

def f3():
	con = None
	try:
		con = pymysql.connect("localhost", "root", "sochosocho", "patient")
		name = entAddPt.get()
		address = entAAddPt.get()
		medical = entMed.get()
		phone = int(entPhone.get())
		args = (name, address, medical, phone)
		cursor = con.cursor()
		sql = "insert into pt values('%s', '%s', '%s', '%d')"
		cursor.execute(sql % args)
		con.commit()
		messagebox.showinfo("Saved", "Patient record inserted")
	
	except Exception as e:
		messagebox.showerror("Bad input", e)
		con.rollback()

	finally:
		if con is not None:
			con.close()

		entAddPt.delete(0, END)
		entAAddPt.delete(0, END)
		entMed.delete(0, END)
		entPhone.delete(0, END)
		entAddPt.focus()

				


def f4():
	adpt.withdraw()
	root.deiconify()



def f5():
	con = None
	try:
		con = pymysql.connect("localhost", "root", "sochosocho", "patient")
		name = entN.get()
		cursor = con.cursor()
		sql = "select * from pt where name = name"
		cursor.execute(sql)
		data = cursor.fetchall()
		messagebox.showinfo(" ",data)

	except Exception as e:
		messagebox.showerror("issue", e)

	finally:
		if con is not None:
			con.close()




def f6():
	vdpt.withdraw()
	root.deiconify()



root = Tk()
root.title("Patient Management System")
root.geometry("500x500+500+500")
root.configure(background = "skyblue")

btnAdd = Button(root, text = "Add-Patient", font = ("arial", 18, "bold italic"), command = f1)
lblAdd = Label(root, text = (msg), font = ("arial", 18, "bold italic"))
btnView = Button(root, text = "View-Patient", font = ("arial", 18, "bold italic"), command = f2)


btnAdd.pack(pady = 10)
btnView.pack(pady = 10)
lblAdd.pack(pady = 10)


adpt = Toplevel(root)
adpt.title("Add-Paitent")
adpt.geometry("500x500+500+500")
adpt.configure(background = "skyblue")
adpt.withdraw()

lblAddPt = Label(adpt, text = "Enter Patient's Name", font = ("arial", 18, "bold italic"))
entAddPt = Entry(adpt, bd = 3.4, font = ("arial", 18, "bold italic"))
lblAAddPt = Label(adpt, text = "Enter Address", font = ("arial", 18, "bold italic"))
entAAddPt = Entry(adpt, bd = 3.4, font = ("arial", 18, "bold italic"))
lblMed = Label(adpt, text = "Enter Patient's Medical History ", font = ("arial", 18, "bold italic"))
entMed = Entry(adpt, bd = 3.4, font = ("arial", 18, "bold italic"))
lblPhone = Label(adpt, text = "Enter Patient's Phone no.", font = ("arial", 18, "bold italic"))
entPhone = Entry(adpt, bd = 3.4, font = ("arial", 18, "bold italic"))
btnSave = Button(adpt, text = "Save", font = ("arial", 18, "bold italic"), command = f3)
btnBack = Button(adpt, text = "Back", font = ("arial", 18, "bold italic"), command = f4)
lblAt = Label(adpt, text = (msg), font = ("arial", 18, "bold italic"))



lblAddPt.pack(pady = 10)
entAddPt.pack(pady = 10)
lblAAddPt.pack(pady = 10)
entAAddPt.pack(pady = 10)
lblMed.pack(pady = 10)
entMed.pack(pady = 10)
lblPhone.pack(pady = 10)
entPhone.pack(pady = 10)
btnSave.pack(pady = 10)
btnBack.pack(pady = 10)
lblAt.pack(pady = 10)




vdpt = Toplevel(root)
vdpt.title("View-Patient")
vdpt.geometry("500x500+500+500")
vdpt.configure(background = "skyblue")
vdpt.withdraw()


lblN = Label(vdpt, text = "Enter Patient's Name", font = ("arial", 18, "bold italic"))
entN = Entry(vdpt, bd = 3.4, font = ("arial", 18, "bold italic"))
btnN = Button(vdpt, text = "View", font = ("arial", 18, "bold italic"), command = f5)
btnB = Button(vdpt, text = "Back", font = ("arial", 18, "bold italic"), command = f6)
lblT = Label(vdpt, text = (msg), font = ("arial", 18, "bold italic"))



lblN.pack(pady = 10)
entN.pack(pady = 10)
btnN.pack(pady = 10)
btnB.pack(pady = 10)
lblT.pack(pady = 10)








root.mainloop()

