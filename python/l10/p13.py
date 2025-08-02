import os.path
import pickle

class student:
	def __init__(self, rno, name):
		self.rno = rno
		self.name = name

	def show(self):
		print("roll no= ", self.rno)
		print("name = ", self.name)
 
list_of_students = []
filename = "students_ka_data.ser"

if os.path.isfile(filename):
	with open(filename, "rb") as f:
		list_of_students = pickle.load(f)
while True:
	op = int(input("1 add, 2 view, 3 delete, 4 exit  "))

	if op == 1:
		rno = int(input("please enter roll no  "))
		name = input("please enter the name  ")
		s = student(rno, name)
		list_of_students.append(s)
		print("record saved  ")

	elif op == 2:
		for d in list_of_students:
			d.show()

	elif op == 3:
		s = int(input("enter the roll no that you want to delete  "))
		list_of_students.clear()
		print(s,"removed")
		

	elif op == 4:
		with open(filename, "wb") as f:
			pickle.dump(list_of_students, f)
		break

	else:
		print("invalid option  ")
