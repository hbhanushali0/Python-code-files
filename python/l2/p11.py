# wapp to find the sum of first n integer numbers

# 5 1+2+3+4+5=15

num = int(input("please enter the integer"))

if num < 0:
	print("B positive")
else:
	sum = 0
	i = 1
	while i <= num:
		sum = sum + i
		i = i + 1
	print("sum = ", sum)
