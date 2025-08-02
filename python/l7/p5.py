# wamdpp for billing generation 

menu = {'idli':20, 'vada':30, 'dosa':25 }
amount = 0.0
while True:
	op = int(input("1 add, 2 amount, 3 exit "))
	if op == 1:
		n = input("please enter food item name ")
		if menu.get(n, -1) == -1:
			print("food item does not exists ")
		else:
			q = int(input("please enter the quantity "))
			amount = amount + menu.get(n) * q
	elif op == 2:			
		print("your amount is", amount)
	elif op == 3:
		break

	else:
		print("invalid option")
