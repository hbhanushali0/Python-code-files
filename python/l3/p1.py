# wapp to find factorial of a number

# i/p: 3	o/p: 1 * 2 * 3 = 6

num = int(input("please enter a number"))

if num < 0:
	print("be positive")
elif num == 0 or num == 1:
	print("answer =", 1)
else:
	fact = 1
	for i in range(1,num+1,1):
		fact = fact * i
	else:
		print("answer = ", fact)
