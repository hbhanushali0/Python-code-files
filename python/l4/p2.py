# wapp to get a menu driven program

import array

data = array.array("i",[])

n = int(input("enter number of elements"))

for i in range(n):
	ele = int(input("enter the elements"))
	
	data.append(ele)

while True:
	
	op = int(input("1) data, 2) ascending, 3) descending, 4) exit "))

	if op == 1:

		for d in data:
			print(d, end=' ')

		print()
	elif op == 2:
	
		# ASCENDING DATA AND DISPLAY

		adata = sorted(data)

		for d in adata:			
			print(d, end=' ')

		print()

	elif op == 3:
		
		# DESCENDING DATA AND DISPLAY

		ddata = sorted(data, reverse=True)
		
		for d in ddata:
			print(d, end=' ')

		print()
	
	elif op == 4:

		break

	else:
		print("invalid option")

