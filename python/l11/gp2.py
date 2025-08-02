

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Even Odd Calci")
root.geometry("400x300+300+100")
root.configure(background = "grey")

def f1():
	try:
		s = entNumber.get()
		num = int(s)
		msg = " "
		if num % 2 == 0:
			msg = "Even "

		else:
			msg = "Odd "

		messagebox.showinfo("Jawab ", msg)

	except ValueError:
		messagebox.showerror("Galat kiya", "int only ")
		entNumber.delete(0, END)
		entNumber.focus()

lblNumber = Label(root, text = "Enter Number  ", font = ("Courier", 20, "bold italic"))
lblNumber.pack(pady=5)

entNumber = Entry(root, bd = 3.5, font = ("Courier", 20, "bold italic"))
entNumber.pack(pady=5)

btnFind = Button(root, bd = 3.5 ,text = "Find ", font = ("Courier", 20, "bold italic"), command = f1)
btnFind.pack(pady=5)

root.mainloop()


	

