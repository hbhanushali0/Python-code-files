from tkinter import *
from tkinter import messagebox

 

win = Tk()
win.title(" What Next ")
win.geometry("400x400+100+100")
win.configure(background = "grey")

sel = IntVar()
sel.set(1)

rbjob = Radiobutton(win, text = "job", font = ("courier", 18, "bold italic"), variable = sel, value = 1)


rbms = Radiobutton(win, text = "Ms", font = ("courier", 18, "bold italic"), variable = sel, value = 2)


rbmba = Radiobutton(win, text = "Mba", font = ("courier", 18, "bold italic"), variable = sel, value = 3)


rbmtech = Radiobutton(win, text = "Mtech", font = ("courier", 18, "bold italic"), variable = sel, value = 4)

rbjob.grid(sticky="W")
rbms.grid(sticky="W")
rbmba.grid(sticky="W")
rbmtech.grid(sticky="W")

def f1():
	res = sel.get()
	if res == 1:
		msg = "Job"

	elif res == 2:
		msg = "Ms"

	elif res == 3:
		msg = "Mba"

	else:
		msg = "Mtech"

	messagebox.showinfo("Selection", msg)

btnsubmit = Button(win, text = "Submit", font = ("courier", 18, "bold italic"), command = f1)
btnsubmit.grid()

win.mainloop()

