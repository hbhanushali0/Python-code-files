# wapp to read tuple of integers from the user and display in descending order


list_data = []
tup_data = ()

reply = input("do you want to add integer yes/no  ")
while reply == "yes":
	ele = int(input("please enter the integer  "))
	list_data.append(ele)
	reply = input("do you want to add more integers yes/no  ")

tup_data = tuple(list_data)
print("before ", tup_data)

list_data.sort(reverse=True)
tup_data = tuple(list_data)
print("after descending ", tup_data)