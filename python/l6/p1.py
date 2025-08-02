# wapp that takes as input integer and returns Ture if the number is Armstrong else 
# returns false


def check(num):
	org_num = num
	sum = 0
	while num > 0:
		digit = num % 10
		sum = sum + digit ** 3
		num = num // 10
	if (sum == org_num):
		return True
	else:
		return False

n = int(input("please enter a number "))

if n < 0:
	print("be positive")
else:
	if check(n):
		print("yes Armstrong number")
	else:
		print("no not an Armstrong number")

