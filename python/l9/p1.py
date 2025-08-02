# wapp to support +, -, * between Book objects

class book:
	def __init__(self, pages):
		self.pages = pages

	def __add__(self, other):
		res = self.pages + other.pages
		return res

	def __sub__(self, other):
		ans = self.pages - other.pages
		return ans

	def __mul__(self, other):
		res = self.pages * other.pages
		return res

b1 = book(200)
b2 = book(300)

r1 = b1 + b2;	print(r1)
r2 = b1 - b2;	print(r2)
r3 = b1 * b2;	print(r3)

