
# user made / user defined Exception

class InvalidrollnoException(Exception):
	def __init__(self, msg):
		self.msg = msg

class InvalidnameException(Exception):
	def __init__(self, msg):
		self.msg = msg

class InvalidmarksException(Exception):
	def __init__(self, msg):
		self.msg = msg




class student:
	def __init__(self, r, n, m):
		self.roll = r
		self.name = n
		self.marks = m
	
	def show(self):
		print("roll no = ", self.roll)
		print("name = ", self.name)
		print("marks = ", self.marks)

try :

	roll = int(input("please enter roll no  "))
	if roll < 0:
		raise InvalidrollnoException("roll no cannot be negative ")
	
	name = input("enter name ")
	if len(name) < 2:
		raise InvalidnameException("name cannot be less than 2 characters")

	marks = int(input("please enter marks  "))
	if marks < 0 or marks > 100:
		raise InvalidmarksException("marks out of range 0 - 100")

	s = student(roll, name, marks)
	s.show()
except Exception as e:
	print("bad input", e)
