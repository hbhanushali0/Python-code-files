# wapp to find factorial of a number non recursively

def fact(n):
	f = 1
	for i in range(1, n+1):
		f = f * i
	else:
		return f
num = int(input("please enter a number "))

if num < 0:
	print("be positive")

elif num == 0 or num == 1:
	print("fact = ", 1)
else:
	res = fact(num)
	print("fact = ", res)
