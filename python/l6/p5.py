# wapp to read list of integers from user and print on screen

num = []

reply = input("do you wish to add integers yes/no  ")
while reply == "yes":
	ele = int(input("enter the integer  "))
	num.append(ele)
	reply = input("do you wish to add more integers yes/no  ")

print(num)


for n in num:
	print(n, end=" ")
print()


for i in range(len(num)):
	print(num[i], end=" ")
print()
