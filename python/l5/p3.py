# wapp to read sentence and sort every word in a sentence
# i/p - kamal classes
# o/p - aaklm acelsss


n = input("enter a sentence ")

l = n.split(" ")

def mysort(s):
	d = sorted(s)
	r = "".join(d)
	return r
new = ""

for d in l:
	new = new + " " + mysort(d)
print("original sentence ", n)

print("new sentence ", new)



