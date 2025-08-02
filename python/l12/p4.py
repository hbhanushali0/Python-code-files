

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Kamal Classes App")
root.geometry("300x500+300+100")
root.configure(background = "grey")

lblName = Label(root, text = "Name", font = ("arial", 18, "bold"))
entName = Entry(root, bd = 3.5, font = ("arial", 18, "bold"), )

lblName.grid()
entName.grid()

lblFeedback = Label(root, text = "Feedback", font = ("arial", 18, "bold"))

f = IntVar()
f.set(1)
rbf = Radiobutton(root, text = "Fantastic", font = ("arial", 18, "bold"), variable = f, value = 1)
rbs = Radiobutton(root, text = "Superb", font = ("arial", 18, "bold"), variable = f, value = 2)
rbe = Radiobutton(root, text = "Excellent", font = ("arial", 18, "bold"), variable = f, value = 3)

lblFeedback.grid()
rbf.grid(sticky = "W")
rbs.grid(sticky = "W")
rbe.grid(sticky = "W")


lblMaterials = Label(root, text = "Materials", font = ("arial", 18, "bold"))

s,n,c = IntVar(), IntVar(), IntVar()

cbSoftware = Checkbutton(root, text = "Software", font = ("arial", 18, "bold"),variable = s)

cbNotes = Checkbutton(root, text = "Notes", font = ("arial", 18, "bold"),variable = n)

cbCertificate = Checkbutton(root, text = "Certificate", font = ("arial", 18, "bold"),variable = c)

lblMaterials.grid()
cbSoftware.grid(sticky = "W")
cbNotes.grid(sticky = "W")
cbCertificate.grid(sticky = "W")

def f1():
	name = entName.get()
	if len(name) < 2 or not name.isalpha():
		messagebox.showerror("Wrong", "invalid name ")
		entName.delete(0, END)
		entName.focus()
		return
	fe = f.get()
	if fe == 1:
		feedback = "Fantastic"
	elif fe == 2:
		feedback = "Superb"
	else:
		feedback = "Excellent"

	Materials = " "
	if s.get() == 1:
		Materials = Materials + "Software"
	if n.get() == 1:
		Materials = Materials + "Notes"
	if c.get() == 1:
		Materials = Materials + "Certificate"

	msg = "Name = " + name + "\nFeedback = " + feedback + "\nMaterials = " + Materials

	messagebox.showinfo("Msg ", msg)
	
	to = "kamalsir@ymail.com"
	subject = "Feedback by" + name
	text = msg
	import smtplib
	sender = "hub8181@gmail.com"
	password = "7875467822"
	message = 'subject: {}\n\n{}'.format(subject, text)
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.ehlo()
	server.login(sender, password)
	print('logged in')
	try:
		server.sendmail(sender, to, message)
		print("email sent")
	except:
		print("error sending email")
	
	server.quit


btnSubmit = Button(root, text = "Submit", font = ("arial", 18, "bold"), command = f1)
btnSubmit.grid()


root.mainloop() 

