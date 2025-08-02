# wapp to read list of marks and find highest and lowest marks


marks = []

reply = input("do you wish to add marks yes/no  ")
while reply == "yes":
	m = int(input("enter marks  "))
	marks.append(m)
	reply = input("do you wish to add more marks yes/no  ")

marks.sort()
lowest = marks[0]
highest = marks[-1]

print("lowest marks = ", lowest, "highest marks = ", highest )
