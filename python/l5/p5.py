
data = "a,2,b,4,c,3"

list = data.split(",")

for i in range(0, len(list), 2):
	w = list[i]
	h = int(list[i+1])
	print((w + "\t") * h)
