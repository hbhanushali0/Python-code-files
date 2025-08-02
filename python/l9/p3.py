# wapp for class employee with IV - eid, ename, epds
# class attendance with IV - nodp

class employee:
	def __init__(self, eid, ename, epds):
		self.eid = eid
		self.ename = ename
		self.epds = epds

	def __mul__(self, other):
		res = self.epds * other.nodp
		return res

class attendance:
	def __init__(self, nodp):
		self.nodp = nodp

e = employee(10, "amit", 500)
a = attendance(25)

sal = e * a
print(sal)