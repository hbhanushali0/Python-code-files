from tkinter import *


root = Tk()
root.title("Colour Me ")
root.geometry("300x400+300+200")
root.configure(background = "grey")

def f1():
	root.configure(background = "red")

def f2():
	root.configure(background = "green")

def f3():
	root.configure(background = "blue")


btnRed = Button(root, text = "red", width = 10, font = ("arial", 18, "bold "), command = f1)

btngreen = Button(root, text = "green", width = 10, font = ("arial", 18, "bold "), command = f2)

btnblue = Button(root, text = "blue", width = 10, font = ("arial", 18, "bold "), command = f3) 

btnRed.pack(pady = 20)
btngreen.pack(pady = 20)
btnblue.pack(pady = 20)


root.mainloop()

