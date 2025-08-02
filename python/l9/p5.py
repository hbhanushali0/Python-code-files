# wapp to read two integer values and perform division use exception handling

print("processing started")

try:
	i = int(input("enter first integer  "))
	a = int(input("enter second integer  "))
	ans = i / a

except ValueError:
	print("integers only")

except ZeroDivisionError:
	print("second number cannot be Zero")
 
except Exception:
	print("check input ")

else:
	print("answer = ", ans)

print("processing ended")
 
	