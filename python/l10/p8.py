# wapp to read data from file if it exists using - with 

import os.path

filename = input("please enter a filename to read  ")

if os.path.exists(filename):
	with open(filename, "r") as f:
		 data = f.read()
		 print(data)
		 print("work done")

else:
	print(filename, "does not exists  ")

