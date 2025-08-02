# wapp to read array of "n" integers from user and count number of positive integers and 

# number of negative integers and number of zeros


import array

data = array.array("i",[])

n = int(input("enter number of elements"))

for i in range(n):
	ele = int(input("enter the elements"))
	
	data.append(ele)

np, nn, nz = 0, 0, 0

for d in data:
	if d > 0:
		np = np + 1
	
	elif d < 0:
		nn = nn + 1

	else:

		nz = nz + 1

print("positive= ", np, "negative= ", nn, "zero= ", nz)

