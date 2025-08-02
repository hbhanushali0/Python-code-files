# wapp to delete file if it exists filename would be provided by user


import os.path

filename = input("please enter a filename ")

if os.path.exists(filename):
	os.remove(filename)
	print(filename, "deleted ")
else:
	print(filename, "does not exists ")
