import tkinter
from tkinter import messagebox
from tkinter import *

def f1():
	root.withdraw()
	ent.deiconify()

def f2():
	ent.withdraw()
	test.deiconify()

def f3():
	ent.withdraw()
	root.deiconify()

def f4():
	if(a.get() == "yes"):
		test.withdraw()
		t1.deiconify()

	else:
		messagebox.showinfo("info", "DON'T WORRY JUST REMAIN HOME QUARANTINE TILL FURTHER NOTICE ")
		test.withdraw()
		ent.deiconify()


def f5():
	if(b.get() == "yes" and c.get() == "yes"):
		messagebox.showinfo("message","YOU MAY HAVE CONTAINED WITH CORONA VIRUS")
		t1.withdraw()
		ent.deiconify()

	else:
		messagebox.showinfo("info", "DON'T WORRY JUST REMAIN HOME QUARANTINE TILL FURTHER NOTICE ")
		t1.withdraw()
		ent.deiconify()





#---------------------------------------------------------------------------------------

root = Tk()
root.geometry("500x500+500+500")
root.configure(background = "grey")
root.title("COVID-19 TESTING APP")

lbl1 = Label(root, text = "Enter your Symptoms to check if you need medical attention or not ", font = ("arial", 18, "bold italic"))

btn1 = Button(root, text = "Enter", font = ("arial", 18, "bold italic"), command = f1)


lbl2 = Label(root, text = "STAY INDOORS| HELP YOURSELF| HELP OTHERS", font = ("arial", 18, "bold italic"))

lbl1.pack(pady = 10)
btn1.pack(pady = 10)
lbl2.pack(pady = 10)

#--------------------------------------------------------------------------------------


ent = Toplevel(root)
ent.geometry("500x500+500+500")
ent.configure(background = "grey")
ent.title("ADD DETAILS")
ent.withdraw()

lbl1 = Label(ent, text = "Enter your Name", font = ("arial", 18, "bold italic"))

ent1 = Entry(ent, bd = 3.5, font = ("arial", 18, "bold italic"))

btn1 = Button(ent, text = "Enter", font = ("arial", 18, "bold italic"), command = f2)

btn2 = Button(ent, text = "Back", font = ("arial", 18, "bold italic"), command = f3)



lbl1.pack(pady = 10)
ent1.pack(pady = 10)
btn1.pack(pady = 10)
btn2.pack(pady = 10)


#--------------------------------------------------------------------------------------

test = Toplevel(ent)
test.geometry("500x500+500+500")
test.configure(background = "grey")
test.title("TESTING QUESTIONS")
test.withdraw()


a = StringVar()







lbl1 = Label(test, text = "Do you have Dry Coughing??", font = ("arial", 18, "bold italic"))

rad1 = Radiobutton(test, text = "yes", font = ("arial", 18, "bold italic"), variable = a, value = "yes")

rad2 = Radiobutton(test, text = "no", font = ("arial", 18, "bold italic"), variable = a, value = "no")

btn1 = Button(test, text = "Save", font = ("arial", 18, "bold italic"), command = f4)

lbl1.pack(pady = 10)
rad1.pack(pady = 10)
rad2.pack(pady = 10)
btn1.pack(pady = 10)



#----------------------------------------------------------------------------------------


t1 = Toplevel(test)
t1.configure(background = "grey")
t1.geometry("500x500+500+500")
t1.title("TESTING QUESTIONS")


b = StringVar()

c = StringVar()



lbl2 = Label(t1, text = "Do you have Fever??", font = ("arial", 18, "bold italic"))
	
rad3 = Radiobutton(t1, text = "yes", variable = b, value = "yes", font = ("arial", 18, "bold italic"))

rad4 = Radiobutton(t1, text = "no", variable = b, value = "no", font = ("arial", 18, "bold italic"))

lbl3 = Label(t1, text = "Do you have body tiredness??", font = ("arial", 18, "bold italic"))

rad5 = Radiobutton(t1, text = "yes", variable = c, value = "yes", font = ("arial", 18, "bold italic"))

rad6 = Radiobutton(t1, text = "no", variable = c, value = "no", font = ("arial", 18, "bold italic"))

btn2 = Button(t1, text = "Check", font = ("arial", 18, "bold italic"), command = f5)



lbl2.pack(pady = 10)
rad3.pack(pady = 10)
rad4.pack(pady = 10)
lbl3.pack(pady = 10)
rad5.pack(pady = 10)
rad6.pack(pady = 10)
btn2.pack(pady = 10)


 	




root.mainloop()
