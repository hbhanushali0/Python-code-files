# wapp to design menu driven program using a function

def area(p1=None, p2=None):
	if p1 is not None and p2 is None:
		ans = 3.1415 * p1 ** 2 
		return ans
	elif p1 is not None and p2 is not None:
		ans = p1 * p2
		return ans
while True:
	op = int(input("1 area of circle 2 area of rectangle 3 exit "))
	if op == 1:
		radius = int(input("please enter radius"))
		ans = area(radius)
		print("area = ", ans)
	elif op == 2:
		length = float(input("please enter length"))
		width = float(input("please enter width"))
		ans = area(length, width)
		print("ans = ", ans)
	elif op == 3:
		break
	else:
		print("invalid option")
		