# wa menu driven python program for stack implementation

import array

stack = array.array("i", [])

while True:
	op = int(input("1 push, 2 pop, 3 peek, 4 display and 5 exit"))

	if op == 1:
		ele = int(input("enter data to push"))
		stack.append(ele)
		print(ele," is inserted")
	elif op == 2:
		if len(stack) == 0:
			print("stack is empty")
		else:
			ele = stack.pop()
		print("popped element is ", ele)
	elif op == 3:
		if len(stack) == 0:
			print("stack is empty")
		else:
			ele = stack[-1]
			print("topmost element is ", e)
	elif op == 4:
		if len(stack) == 0:
			print("stack is empty")
		else:
			print(stack)
	elif op == 5:
		break
	else:
		print("invalid syntax")

 