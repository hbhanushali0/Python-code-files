# waoopp for class circle where IV is radius and IM are display, area and circumference

class circle():
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		ans = 3.14159 * radius ** 2
		print("area = ", round(ans, 2))
	
	def circumference(self):
		cir = 2 * 3.14159 * radius
		print("circumference = ", round(cir, 2))

	def display(self):
		print("radius = ", self.radius)

radius = float(input("please enter the radius "))
c = circle(radius)
c.display()
c.area()
c.circumference()

