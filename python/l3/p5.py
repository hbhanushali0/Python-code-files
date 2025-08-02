# wapp to generate
# a a a a
# b b b
# c c
# d

num = int(input("please enter lines of pattern"))

if num < 0:
	print("be positive")
else:
	ch = 97
	for i in range(num, 0, -1):
		print(i * (chr(ch) + " "))
		ch = ch + 1

