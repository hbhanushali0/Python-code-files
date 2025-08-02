# wapp using a function to generate all 3 digit Armstrong number


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

for i in range(100, 1000):
	if check(i):
		print(i)

 