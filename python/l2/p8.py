# wapp to read three integers and find the maximum

n1 = int(input("please enter first number"))

n2 = int(input("please enter second number"))

n3 = int(input("please enter third number"))

if n1 > n2:
	max = n1
else:
	max = n2
if n3 > max:
	max = n3
print("maximum number is ", max)


	