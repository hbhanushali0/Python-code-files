# wapp to read and reverse the sentence with every word too reversed
# i/p - kamal classes thane
# o/p - enact sessalc lamak

n = input("enter a sentence ")

d = n.split(" ")

new = ""

for l in d:
	# reverse every word and reverse the sentence also
	new = l[::-1] + " " + new

print("original sentence", n)

print("new sentence", new)



