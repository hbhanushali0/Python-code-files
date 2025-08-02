
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import mysql
import pymysql
import socket
import requests
import bs4

try:
	socket.create_connection(("www.google.com", 80))
	res = requests.get("http://ipinfo.io")
	data = res.json()
	city = data["region"]
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=" + city
	a3 = "&appid=c6e315d09197cec231495138183954bd"
	api_address = a1 + a2 + a3
	res1 = requests.get(api_address)
	print(res1)
	data = res1.json()
	main = data["main"]
	temp = main["temp"]
	print("temp = ", temp)


	res = requests.get("http://www.brainyquote.com/quotes_of_the_day.html")
	soup = bs4.BeautifulSoup(res.text, 'lxml')

	quote = soup.find('img', {"class": "p-qotd"})
	msg = quote['alt']


	

except Exception as e:
	messagebox.showerror("Bad Network",e)

def getRegion():
	region = "Region = " + city
	return region

def getTemperature():
	temperature = "Temperature = " + str(temp)
	return temperature
	

def f1():
	root.withdraw()
	adst.deiconify()


def f2():
	stViewData.delete(1.0, END)
	root.withdraw()
	vist.deiconify()
	con = None
	try:
		con = pymysql.connect("localhost", "root", "sochosocho", "student1")
		cursor = con.cursor()
		sql = "select rno, name, marks from stud "
		cursor.execute(sql)
		data = cursor.fetchall()
		msg = " "
		for d in data:
			msg = msg + "rno = " +str(d[0]) + "name = " +str(d[1]) + "marks = " +str(d[2]) + "\n"
		stViewData.insert(INSERT, msg)

	except Exception as e:
		messagebox.showerror("issue", e)

	finally:
		if con is not None:
			con.close()


def f3():
	root.withdraw()
	upst.deiconify()


def f4():
	root.withdraw()
	dest.deiconify()

def f5():
	con = None
	try:
		con = pymysql.connect("localhost", "root", "sochosocho", "student1")
		cursor = con.cursor()
		sql = "select name, marks from student1"
		cursor.execute(sql)
		data = cursor.fetchall()
		if len(data):
			import pandas as pd
			import matplotlib.pyplot as plt
			import numpy as np
			names = []
			marks = []
			for d in data:
				names.append(d[0])
				marks.append(d[1])
			x = np.arange(len(names))
			bars = plt.bar(x, marks, label = "Marks", width = 0.2)
			plt.xticks(x,names)
			plt.legend()
			plt.grid()
			for bar in bars:
				vval = bar.get_height()
				plt.text(bar.get_x(), yval + .005, yval)
			plt.xlabel("Names")
			plt.ylabel("Marks")
			plt.title("Marks Graph")
			plt.show()
		else:
			messagebox.showwarning("Warning", "No record available")
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("issue", str(e))
	finally:
		if con is not None:
			con.close()



def f6():
	con = None
	try:
		con = pymysql.connect("localhost", "root", "sochosocho", "student1")
		if len(entAddRno.get())==0:
			raise messagebox.showwarning("Issue","Please enter rno")
		if len(entAddName.get())==0:
			raise messagebox.showwarning("Issue","Please enter Name")
		if len(entAddMarks.get())==0:
			raise messagebox.showwarning("Issue","Please Enter Marks")
		if entAddRno.get().lstrip('-').isdigit()==True:
			rno = int(entAddRno.get())
		else:
			entAddRno.delete(0,END)
			entAddRno.focus()
			raise messagebox.showerror("Error","Rno cannot contain alphabets")
			rno = int(entAddRno.get())
		if int(rno) <= 0:
			entAddRno.delete(0,END)
			entAddRno.focus()
			raise messagebox.showerror("Error","Rno should be positive")
		cursor = con.cursor()
		sql = "select rno from student where rno='%d'"	
		cursor.execute(sql % rno)
		data = cursor.fetchall()
		if len(data):				
			entAddRno.delete(0,END)
			entAddRno.focus()
			messagebox.showerror("Error","Record Already Exists")
		if entAddName.get().isalpha()==True:
			name = entAddName.get()
		else:
			entAddName.delete(0,END)
			entAddName.focus()
			raise messagebox.showerror("Error","Invalid Name")
		if len(name)<2:
			entAddName.delete(0,END)
			entAddName.focus()
			raise messagebox.showerror("Error","Invalid name")
		if entAddMarks.get().lstrip('-').isdigit()==True:
			marks = int(entAddMarks.get())
		else:
			entAddMarks.delete(0,END)
			entAddMarks.focus()
			raise messagebox.showerror("Error","Marks should be in integer")
		if marks < 0 or marks > 100:
			entAddMarks.delete(0,END)
			entAddMarks.focus()
			raise messagebox.showerror("Error","Invalid Marks")
		sql = "insert into student_info values('%d','%s','%d')"
		args = (rno,name,marks)
		cursor.execute(sql % args)
		con.commit()
		messagebox.showinfo("Correct ", "rows inserted")

	except Exception as e:
		messagebox.showerror("Bad Input", e)
		con.rollback()

	finally:
		if con is not None:
			con.close()

		entAddRno.delete(0, END)
		entAddName.delete(0, END)
		entAddMarks.delete(0, END)
		entAddRno.focus()
		

def f7():
	adst.withdraw()
	root.deiconify()


def f8():
	vist.withdraw()
	root.deiconify()



def f9():
	con = None
	try:
		con = pymysql.connect("localhost", "root", "sochosocho", "student1")
		newrno = int(entupRno.get())
		newname = entupName.get()
		newmarks = int(entupMarks.get())
		args = (newrno , newname , newmarks)
		cursor = con.cursor()
		sql = "update stud set rno = %d , name = %s , marks = %d where rno = '%d'"
		cursor.execute(sql % args)
		con.commit()
		messagebox.showinfo("Correct ", "Updated")
	
	except Exception as e:
		messagebox.showerror("Bad input", e)
		con.rollback()

	finally:
		if con is not None:
			con.close()

		entupRno.delete(0, END)
		entupName.delete(0, END)
		entupMarks.delete(0, END)
		entupRno.focus()



def f10():
	upst.withdraw()
	root.deiconify()


def f11():
	con = None
	try:
		con = pymysql.connect("localhost", "root", "sochosocho", "student1")
		delrno = int(entdeRno.get())
		args = (delrno)
		cursor = con.cursor()
		sql = "delete from stud where rno = %d "
		cursor.execute(sql % args)
		con.commit()
		messagebox.showinfo("Correct", "Deleted ")

	except Exception as e:
		messagebox.showerror("Bad input", e)
		con.rollback()

	finally:
		if con is not None:
			con.close()
		
		entdeRno.delete(0, END)
		entdeRno.focus()
		


def f12():
	dest.withdraw()
	root.deiconify()






root = Tk()
root.title("Student Management System")
root.geometry("500x500+500+500")
root.configure(background = "grey")

btnAdd = Button(root, text = "Add", font = ("arial", 18, "bold italic"), command = f1)
btnView = Button(root, text = "View", font = ("arial", 18, "bold italic"),command = f2)
btnUpdate = Button(root, text = "Update", font = ("arial", 18, "bold italic"), command = f3)
btnDelete = Button(root, text = "Delete", font = ("arial", 18, "bold italic"), command = f4)
btnGraph = Button(root, text = "Graph", font = ("arial", 18, "bold italic"),command = f5)

lblTemp = Label(root, text = (getRegion(), getTemperature()), font = ("arial", 18, "bold italic"))
lblquote = Label(root, text = (msg), font = ("arial", 18, "bold italic"))

btnAdd.pack(pady = 10)
btnView.pack(pady = 10)
btnUpdate.pack(pady = 10)
btnDelete.pack(pady = 10)
btnGraph.pack(pady = 10)

lblTemp.pack(pady = 10)
lblquote.pack(pady = 10)



adst = Toplevel(root)
adst.title("ADD STUDENT")
adst.geometry("500x500+500+500")
adst.configure(background = "grey")
adst.withdraw()


lblAddRno = Label(adst, text = "Enter Roll no", font = ("arial", 18, "bold italic"))
entAddRno = Entry(adst, bd = 3.4, font = ("arial", 18, "bold italic"))
lblAddName = Label(adst, text = "Enter Name ", font = ("arial", 18, "bold italic"))
entAddName = Entry(adst, bd = 3.4, font = ("arial", 18, "bold italic"))
lblAddMarks = Label(adst, text = "Enter Marks", font = ("arial", 18, "bold italic"))
entAddMarks = Entry(adst, bd = 3.5, font = ("arial", 18, "bold italic"))
btnAddSave = Button(adst, text = "Save", font = ("arial", 18, "bold italic"), command = f6)
btnAddBack = Button(adst, text = "Back", font = ("arial", 18, "bold italic"), command = f7)


lblAddRno.pack(pady = 10)
entAddRno.pack(pady = 10)
lblAddName.pack(pady = 10)
entAddName.pack(pady= 10)
lblAddMarks.pack(pady = 10)
entAddMarks.pack(pady = 10)
btnAddSave.pack(pady = 10)
btnAddBack.pack(pady = 10)


vist = Toplevel(root)
vist.title("VIEW ")
vist.geometry("500x500+500+500")
vist.configure(background = "grey")
vist.withdraw()


stViewData = scrolledtext.ScrolledText(vist, width = 30, height = 10)
btnViewBack = Button(vist, text = "Back", font = ("arial", 18, "bold italic"), command = f8)

stViewData.pack(pady = 10)
btnViewBack.pack(pady = 10)



upst = Toplevel(root)
upst.title("UPDATE STUDENT ")
upst.geometry("500x500+500+500")
upst.configure(background = "grey")
upst.withdraw()


lblupRno = Label(upst, text = "Enter Roll No. ", font = ("arial", 18, "bold italic"))
entupRno = Entry(upst, bd = 3.5, font = ("arial", 18, "bold italic"))
lblupName = Label(upst, text = "Enter Name ", font = ("arial", 18, "bold italic"))
entupName = Entry(upst, bd = 3.5, font = ("arial", 18, "bold italic"))
lblupMarks = Label(upst, text = "Enter Marks ", font = ("arial", 18, "bold italic"))
entupMarks = Entry(upst, bd = 3.5, font = ("arial", 18, "bold italic"))
btupSave = Button(upst, text = "Save ", font = ("arial", 18, "bold italic"), command = f9)
btupBack = Button(upst, text = "Back ", font = ("arial", 18, "bold italic"), command = f10)


lblupRno.pack(pady = 10)
entupRno.pack(pady = 10)
lblupName.pack(pady = 10)
entupName.pack(pady = 10)
lblupMarks.pack(pady = 10)
entupMarks.pack(pady = 10)
btupSave.pack(pady = 10)
btupBack.pack(pady = 10)




dest = Toplevel(root)
dest.title("DELETE ")
dest.geometry("500x500+500+500")
dest.configure(background = "grey")
dest.withdraw()



lbldeRno = Label(dest, text = "Enter Roll No ", font = ("arial", 18, "bold italic"))
entdeRno = Entry(dest, bd = 3.5, font = ("arial", 18, "bold italic"))
btdeDelete = Button(dest, text = "Delete", font = ("arial", 18, "bold italic"), command = f11)
btdeBack = Button(dest, text = "Back", font = ("arial", 18, "bold italic"), command = f12)


lbldeRno.pack(pady = 10)
entdeRno.pack(pady = 10)
btdeDelete.pack(pady = 10)
btdeBack.pack(pady = 10)



lblCity=Label(root,text='City:',font=('arial', 16, 'bold italic'))
lblCityRslt=Label(root,text=CityRslt,font=('arial', 16, 'bold italic'))
lblTemp=Label(root,text='Temp:',font=('arial', 16, 'bold italic'))
lblTempRslt=Label(root,text=f13(),font=('arial', 16, 'bold italic'))
lblQotd=Label(root,text='QOTD:',font=('arial', 16, 'bold italic'))
lblQotdRslt=Label(root,text=QotdRslt,font=('arial', 16, 'bold italic'))

lblCity.place(x=230,y=380)
lblCityRslt.place(x=310,y=380)
lblTemp.place(x=800,y=380)
lblTempRslt.place(x=880,y=380)
lblQotd.place(x=60,y=440)
lblQotdRslt.place(x=150,y=440)








root.mainloop()


