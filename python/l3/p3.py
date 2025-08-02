# wapp to generate 
# A
# B B
# C C C
# D D D D

num = int(input("please enter lines of pattern"))

if num < 0:
	print("be psitive")
else:
	ch = 65
	for i in range(1, num + 1):
		print(i * (chr(ch) + " "))
		ch = ch + 1
