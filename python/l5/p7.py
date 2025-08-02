# wapp to find factorial of a number recursively

def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n - 1)

num = int(input("please enter a number "))

if num < 0:
	print("be positive")

elif num == 0 or num == 1:
	print("fact = ", 1)
else:
	res = fact(num)
	print("fact = ", res)