# wa menu driven program to maintain the runs scored by player - dict{}


score_card = {}
while True:
	op = int(input("1 add, 2 view, 3 update, 4 delete, 5 exit "))
	if op == 1:
		name = input("enter player name ")
		if score_card.get(name, -1) == -1:
			runs = int(input("enter runs scored "))
			score_card[name] = runs
			print(name, "added")
		else:
			print(name, "already exists ")
	elif op == 2:
		for n in score_card:
			print("name", n, "runs", score_card[n])
	elif op == 3:		 
		name = input("enter player name ")
		if score_card.get(name, -1) == -1:
			print(name, "does not exists ")
		else:
			runs = int(input("enter new runs  "))
			score_card[name] = runs
			print(name, "updated ")
	elif op == 4:
		name = input("enter player name ")
		if score_card.get(name, -1) == -1:
			print(name, "does not exists ")
		else:
			score_card.pop(name)
			print(name, "deleted ")
	
	elif op == 5:
		break

	else:
		print("invalid option")

