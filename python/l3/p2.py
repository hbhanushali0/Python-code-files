# wapp to generate 
# *
# * *
# * * *
# * * * * where lines of pattern are provided by user

num = int(input("please enter number of lines"))

if num < 0:
	print("be positive")
else:
	for i in range(1,num + 1):
		print(i * "* ")
