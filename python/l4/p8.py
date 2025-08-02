# wapp to read username and password
import getpass
username = input("enter username")
password = getpass.getpass("enter password")

if((username=='antman')and (password=='batman')):
	print("welcome")
else:
	print("try again")

