# wapp to generate
# * * * *
# * * *
# * *
# *

num = int(input("please enter number of lines of pattern"))

if num < 0:
	print("be positive")
else:
	for i in range(num, 0, -1):
		print(i * "* ")
