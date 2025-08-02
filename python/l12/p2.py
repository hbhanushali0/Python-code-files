from tkinter import *


root = Tk()
root.title("Colour Me ")
root.geometry("400x400+100+100")
root.configure(background = "grey")

def f(num):
	if num == 1:
		root.configure(background = "red")
	
	elif num == 2:
		root.configure(background = "green")

	else:
		root.configure(background = "blue")


btnRed = Button(root, text = "red", width = 10, font = ("arial", 18, "bold "), command = lambda:f(1))

btngreen = Button(root, text = "green", width = 10, font = ("arial", 18, "bold "), command = lambda:f(2))

btnblue = Button(root, text = "blue", width = 10, font = ("arial", 18, "bold "), command = lambda:f(3)) 

btnRed.place(x = 10, y = 100)
btngreen.place(x = 100, y = 50)
btnblue.place(x = 200, y = 100)


root.mainloop()

