# wapp to accept Command Line Arguments and receive two integers and perform ans = n1 / n2


try :
	import sys
	n1 = int(sys.argv[1])
	n2 = int(sys.argv[2])
	ans = n1 / n2

except IndexError:
	print("integers only")

except ValueError:
	print("integers only")

except ZeroDivisionError:
	print("second number cannot be Zero")

except Exception as e:
	print("some other issue", e)

else :
	print("ans = ", ans)

finally :
	print("mission completed")


