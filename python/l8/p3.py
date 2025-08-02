# wamdoopp for class employee:
# where IV: eid, ename, esalary PI: eid,ename,esalary
# IM: show calc_bonus SV: ecount SM: show_ecount

class employee:
	ecount = 0
	def __init__(self, eid, ename, esalary):
		self.eid = eid
		self.ename = ename
		self.esalary = esalary
		employee.ecount = employee.ecount + 1
	
	def show(self):
		print("eid = ", self.eid)
		print("ename = ", self.ename)
		print("esalary = ", self.esalary)

	def calc_bonus(self):
		ans = self.esalary * 0.10
		print("bonus amt = ", round(ans, 2))
	
	@staticmethod
	def show_ecount():
		print("employee count ", employee.ecount)

list_of_emp = []

while True:

	op = int(input("1 add, 2 view, 3 delete, 4 exit"))
	if op == 1:
		eid = int(input("enter the id  "))
		ename = input("enter the name  ")
		esalary = float(input("enter the salary  "))
		e = employee(eid,ename,esalary)
		list_of_emp.append(e)

	elif op == 2:
		employee.show_ecount()
		for e in list_of_emp:
			print("*" * 40)
			e.show()

	elif op == 3:
		eid = int(input("enter the id you want to remove"))
		for e in list_of_emp:
			if e.eid == eid:
				list_of_emp.remove(e)
				print(eid,"removed")
				employee.ecount = employee.ecount - 1
	
	elif op == 4:
		break

	else:
		print("invalid option")

