from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from sqlite3 import *
import socket

root = Tk()
root.title("Student Management System")
root.geometry("1200x500+150+150")
root.configure(background="pink")

def f1():
	root.withdraw()
	adst.deiconify()
	entAddRno.focus()

def f2():
	entAddRno.delete(0 ,END)
	entAddName.delete(0, END)
	entAddMarks.delete(0, END)
	adst.withdraw()
	root.deiconify()

def f3():
	stdata.delete(1.0, END)
	root.withdraw()
	vist.deiconify()
	con = None
	try:
		con = connect("student.db")
		cursor = con.cursor()
		sql = "select rno, name, marks from student_info"
		cursor.execute(sql)
		data = cursor.fetchall()
		if len(data):
			msg = " "
			for d in data:
				msg = msg + "rno:" + str(d[0]) + " name: "+ str(d[1]) + " marks:"+ str(d[2]) +"\n"
			stdata.insert(INSERT, msg)
		else:
			strdata.insert(INSERT,"No records found")
	except DatabaseError as e:
		messagebox.showerror("issue",str(e))
	finally:
		if con is not None:
			con.close()

def f4():
	vist.withdraw()
	root.deiconify()

def f5():
	root.withdraw()
	upst.deiconify()
	entUpdRno.focus()

def f6():
	entUpdRno.delete(0 ,END)
	entUpdName.delete(0, END)
	entUpdMarks.delete(0, END)
	upst.withdraw()
	root.deiconify()

def f7():
	root.withdraw()
	dlst.deiconify()
	entDltRno.focus()

def f8():
	entDltRno.delete(0 ,END)
	dlst.withdraw()
	root.deiconify()

def f9():
	con = None
	try:
		con = connect("student.db")
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
		sql = "select rno from student_info where rno='%d'"
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
		messagebox.showinfo("Success","record inserted")
		entAddRno.delete(0,END)
		entAddName.delete(0,END)
		entAddMarks.delete(0,END)
		entAddRno.focus()
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("issue",str(e))
	finally:
		if con is not None:
			con.close()

def f10():
	con = None
	try:
		con = connect("student.db")
		if len(entUpdRno.get())==0:
			raise messagebox.showwarning("Issue","Please enter roll number")
		if len(entUpdName.get())==0:
			raise messagebox.showwarning("Issue","Please Enter Name")
		if len(entUpdMarks.get())==0:
			raise messagebox.showwarning("Issue","Please Enter Marks ")
		if entUpdRno.get().lstrip('-').isdigit() == True:
			rno = int(entUpdRno.get())
		else:
			entUpdRno.delete(0 ,END)
			entUpdRno.focus()
			raise messagebox.showerror("Error","Invalid Roll Number")
			rno = int(entUpdRno.get())
		if int(rno) <= 0:
			entUpdRno.delete(0 ,END)
			entUpdRno.focus()
			raise messagebox.showerror("Error","Roll No cannot be Negative")
		cursor = con.cursor()
		sql = "select rno from student_info where rno='%d'"
		cursor.execute(sql % rno)
		data = cursor.fetchall()
		if len(data):
			pass
		else:
			entUpdRno.delete(0,END)
			entUpdRno.focus()
			raise messagebox.showerror("Error","Record does not exists")		
		if entUpdName.get().isalpha()==True:
			name =entUpdName.get()
		else:
			entUpdName.delete(0,END)
			entUpdName.focus()
			raise messagebox.showerror("Error","Invalid Name")
		if len(name) < 2:
			entUpdName.delete(0,END)
			entUpdName.focus()
			raise messagebox.showerror("Error","Name must be of atleast 2 characters")
		if entUpdMarks.get().lstrip('-').isdigit()==True:
			marks=int(entUpdMarks.get())
		else:
			entUpdMarks.delete(0,END)
			entUpdMarks.focus()
			raise messagebox.showerror("Error","Marks cannot contain alphabets")
		if marks < 0 or marks > 100:
			entUpdMarks.delete(0,END)
			entUpdMarks.focus()
			raise messagebox.showerror("Error","Invalid Marks Entered")
		sql = "update student_info set rno = '%d',name = '%s',marks = '%d' where rno = '%d'"
		args = (rno,name,marks,rno)
		cursor.execute(sql % args)
		con.commit()
		messagebox.showinfo("Success","record Updated")
		entUpdRno.delete(0 ,END)
		entUpdName.delete(0, END)
		entUpdMarks.delete(0, END)
		entUpdRno.focus()
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("issue",str(e))
	finally:
		if con is not None:
			con.close()

def f11():
	con = None
	try:
		con = connect("student.db")
		if entDltRno.get().lstrip('-').isdigit() == True:
			rno = int(entDltRno.get())
		else:
			raise messagebox.showerror("Error","roll no cannot contain alphabets")
		if len(entDltRno.get())==0:
			raise messagebox.showwarning("Issue","Please enter rno")
		if int(rno) <= 0:
			raise messagebox.showerror("Error","Roll No cannot be Negative")
		cursor = con.cursor()
		sql = "select rno from student_info where rno='%d'"
		cursor.execute(sql % rno)
		data = cursor.fetchall()
		if len(data):
			sql = "delete from  student_info where rno = '%d'"
			cursor.execute(sql % rno)
			con.commit()	
			messagebox.showinfo("Success","record Deleted")
		else:
			messagebox.showwarning("Warning","Record does not exists")
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("issue",str(e))
	finally:
		entDltRno.delete(0 ,END)
		entDltRno.focus()
		if con is not None:
			con.close()

 
def f12():
	import requests
	import socket
	try:
		socket.create_connection(("www.google.com",80))
		res = requests.get("https://ipinfo.io")
		data = res.json()
		city = data['city']
		return str(city)
	except OSError:
		return ("Not-Available")
 
def f13():
	import requests
	import socket
	try:
		socket.create_connection(("www.google.com",80))
		res = requests.get("https://ipinfo.io")
		data = res.json()    
		city = data['city']
		a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
		a2 = "&q=" + city
		a3 = "&appid=c6e315d09197cec231495138183954bd"
		api_address = a1 + a2 + a3
		res = requests.get(api_address)
		data = res.json()
		temp = data['main']['temp']
		return(temp)
	except OSError :
		return("Not-Available")
	except KeyError:
		return("Not-Available")

# def f14():
	#import bs4
	#import requests
	#res  = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
	#soup = bs4.BeautifulSoup(res.text , 'lxml')
	#quote = soup.find('img', {"class":"p-qotd"})
	#msg = quote['alt']
	#return(msg)

def f15():
	con = None
	try:
		con = connect("student.db")
		cursor = con.cursor()
		sql = "select name,marks from student_info"	
		cursor.execute(sql)
		data = cursor.fetchall()
		if len(data):
			import pandas as pd
			import matplotlib.pyplot as plt
			import numpy as np
			names=[]
			marks=[]
			for d in data:
				names.append(d[0])
				marks.append(d[1])
			x = np.arange(len(names))
			bars = plt.bar(x , marks,label='Marks',width=0.2)
			plt.xticks(x,names)
			plt.legend()
			plt.grid()
			for bar in bars:
			    yval = bar.get_height()
			    plt.text(bar.get_x(), yval + .005, yval)
			plt.xlabel("Names")
			plt.ylabel("Marks")
			plt.title("Marks Graph")
			plt.show()
		else:
			messagebox.showwarning("Warning","No record available")
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("issue",str(e))
	finally:
		if con is not None:
			con.close()

CityRslt=f12()
TempRslt=f13()
#QotdRslt=f14()

btnAdd = Button(root, text="Add", font=('comic sans ms', 16, 'bold'), width=10, command=f1)
btnView = Button(root, text="View", font=('comic sans ms', 16, 'bold'), width=10, command=f3)
btnUpdate = Button(root, text="Update", font=('comic sans ms', 16, 'bold'), width=10, command=f5)
btnDelete = Button(root, text="Delete", font=('comic sans ms', 16, 'bold'), width=10, command=f7)
btnGraph = Button(root, text="Graph", font=('comic sans ms', 16, 'bold'), width=10, command=f15)
btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnGraph.pack(pady=10)

adst = Toplevel(root)
adst.title("Add Student")
adst.geometry("1200x500+150+150")

lblAddRno = Label(adst, text="enter rno", font=('comic sans ms', 16, 'bold')) 
entAddRno = Entry(adst, bd=5, font=('comic sans ms', 16, 'bold'))

lblAddName = Label(adst, text="enter name", font=('comic sans ms', 16, 'bold'))
entAddName = Entry(adst, bd=5, font=('comic sans ms', 16, 'bold'))

lblAddMarks = Label(adst, text="enter marks", font=('comic sans ms', 16, 'bold'))
entAddMarks = Entry(adst, bd=5, font=('comic sans ms', 16, 'bold'))

btnAddSave = Button(adst, text="Save", font=('comic sans ms', 16, 'bold'), command=f9)
btnAddBack = Button(adst, text="Back", font=('comic sans ms', 16, 'bold'), command=f2)

lblAddRno.pack(pady=10)
entAddRno.pack(pady=10)
lblAddName.pack(pady=10)
entAddName.pack(pady=10)
lblAddMarks.pack(pady=10)
entAddMarks.pack(pady=10)
btnAddSave.pack(pady=10)
btnAddBack.pack(pady=10)

adst.withdraw()

vist = Toplevel(root)
vist.title("View Student")
vist.geometry("1200x500+150+150")

stdata = scrolledtext.ScrolledText(vist, width=60, height=20)
btnViewBack = Button(vist, text="Back", font=('comic sans ms', 16, 'bold'),command=f4)

stdata.pack(pady=10)
btnViewBack.pack(pady=10)

vist.withdraw()

upst = Toplevel(root)
upst.title("Update Student")
upst.geometry("1200x500+150+150")

lblUpdRno = Label(upst, text="enter rno", font=('comic sans ms', 16, 'bold')) 
entUpdRno = Entry(upst, bd=5, font=('comic sans ms', 16, 'bold'))

lblUpdName = Label(upst, text="enter name", font=('comic sans ms', 16, 'bold'))
entUpdName = Entry(upst, bd=5, font=('comic sans ms', 16, 'bold'))

lblUpdMarks = Label(upst, text="enter marks", font=('comic sans ms', 16, 'bold'))
entUpdMarks = Entry(upst, bd=5, font=('comic sans ms', 16, 'bold'))

btnUpdSave = Button(upst, text="Save", font=('comic sans ms', 16, 'bold'), command=f10)
btnUpdBack = Button(upst, text="Back", font=('comic sans ms', 16, 'bold'), command=f6)

lblUpdRno.pack(pady=10)
entUpdRno.pack(pady=10)
lblUpdName.pack(pady=10)
entUpdName.pack(pady=10)
lblUpdMarks.pack(pady=10)
entUpdMarks.pack(pady=10)
btnUpdSave.pack(pady=10)
btnUpdBack.pack(pady=10)

upst.withdraw()

dlst = Toplevel(root)
dlst.title("Delete Student")
dlst.geometry("1200x500+150+150")

lblDltRno = Label(dlst, text="enter rno", font=('comic sans ms', 16, 'bold')) 
entDltRno = Entry(dlst, bd=5, font=('comic sans ms', 16, 'bold'))

btnDltSave = Button(dlst, text="Save", font=('comic sans ms', 16, 'bold'), command=f11)
btnDltBack = Button(dlst, text="Back", font=('comic sans ms', 16, 'bold'), command=f8)

lblDltRno.pack(pady=20)
entDltRno.pack(pady=10)
btnDltSave.pack(pady=30)
btnDltBack.pack(pady=10)

dlst.withdraw()

lblCity=Label(root,text='City:',font=('comic sans ms', 16, 'bold'))
lblCityRslt=Label(root,text=CityRslt,font=('comic sans ms', 16, 'bold'))
lblTemp=Label(root,text='Temp:',font=('comic sans ms', 16, 'bold'))
lblTempRslt=Label(root,text=f13(),font=('comic sans ms', 16, 'bold'))
lblQotd=Label(root,text='QOTD:',font=('comic sans ms', 16, 'bold'))
#lblQotdRslt=Label(root,text=QotdRslt,font=('comic sans ms', 16, 'bold'))

lblCity.place(x=230,y=380)
lblCityRslt.place(x=310,y=380)
lblTemp.place(x=800,y=380)
lblTempRslt.place(x=880,y=380)
lblQotd.place(x=60,y=440)
#lblQotdRslt.place(x=150,y=440)



root.mainloop()
