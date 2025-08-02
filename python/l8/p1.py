# waoopp for class rectangle:
# IV: length and width
# IM: show() for showing length and width
# IM: area() for area of rect
# IM: perimeter() for perimeter of rect

class rectangle:
	def __init__(self, le, wi):
		self.length = le
		self.width = wi

	def show(self):
		print("length is ", self.length)
		print("width is ", self.width)

	def area(self):
		ans = self.length * self.width
		print("area = ", ans)
	
	def perimeter(self):
		peri = 2 * (self.length + self.width) 
		print("perimeter = ", peri)

length = float(input("please enter the length  "))
width = float(input("please enter the width  "))
r = rectangle(length, width)
r.show()
r.area()
r.perimeter()

