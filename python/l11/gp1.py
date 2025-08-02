# gui app building

from tkinter import *
from datetime import *
from tkinter import messagebox
from webbrowser import *

root = Tk()
root.title("D n T App")
root.geometry("400x300+300+100")
root.configure(background = "light blue")

def f1():
	date = datetime.now().date()
	messagebox.showinfo("date", date)

def f2():
	time = datetime.now().time()
	messagebox.showwarning("time", time)

def f3():
	dt = datetime.now()
	messagebox.showerror("DT & TI ", dt)

def f4():
	open("www.apple.com")

btnDate = Button(root, text = "Date ", width =10, font = ("arial", 18, "italic"), command = f1)
btnTime = Button(root, text = "Time ", width =10, font = ("arial", 18, "italic"), command = f2)
btnDateTime = Button(root, text = "DT & TI ", width =10, font = ("arial", 18, "italic"), command = f3)
btnVisitUs = Button(root, text = "Visit Us ", width =10, font = ("arial", 18, "italic"), command = f4)


btnDate.pack(pady=10)
btnTime.pack(pady=10)
btnDateTime.pack(pady=10)
btnVisitUs.pack(pady=10)


root.mainloop()


