# wapp to find the sum of the digits

num = int(input("please enter the digits"))

if num < 0:
	print("Be Positive")
else:
	sum = 0
	while num > 0:
		digit = num % 10
		sum = sum + digit
		num = num // 10
	print("sum = ", sum)
