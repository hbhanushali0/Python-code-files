# wapp for class mech with IV - price - m = mech()
# class bee with IV - amount - b = bee()

class mech:
	def __init__(self, price):
		self.price = price
	
	def __add__(self, other):
		res = self.price + other.amount
		return res

	def __mul__(self, other):
		ans = self.price * other.amount
		return ans
class bee:
	def __init__(self, amount):
		self.amount = amount

	def __sub__(self, other):
		res = self.amount - other.price
		return res

m = mech(750)
b = bee(350)

r1 = m + b;	print(r1)
r2 = b - m;	print(r2)
r3 = m * b;	print(r3)

