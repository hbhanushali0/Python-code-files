# wapp to read year and find if its a leap year

year = int(input("please enter an year"))

b1 = (year%100 != 0) and (year%4 == 0)	# every 4 years

b2 = (year%100 == 0) and (year%400 == 0)	# every 400 years

if b1 or b2:
	print("leap year")

else:
	print("not a leap year")
