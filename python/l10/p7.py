# wapp to write a data into file if it exists else filename and data given by user

import os.path

filename = input("please enter a filename  ")

if os.path.isfile(filename):
	f = None
	try:
		f = open(filename, "a")
		data = input("please enter data to write  ")
		f.write(data + "\n")
		print("work done")

	except Exception as e:
		print("issue", e)
	
	finally:
		if f is not None:
			f.close()

else:
	print(filename, "does not exists ")


	 
 