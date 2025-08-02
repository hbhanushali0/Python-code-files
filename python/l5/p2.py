# wapp to read two strings from user and check if they are anagrams
# anagrams - characters are same but meanings are different
# e.g. - listen & silent
# e.g. - madam curie & radium came using function


def mysort(s):
	d = sorted(s)
	r = "".join(d)
	return r

n1 = input("enter a string  ")

n2 = input("enter the second string  ")

ns1 = mysort(n1)

ns2 = mysort(n2)

if ns1 == ns2:
	print("yes they are anagrams")
else:
	print("no they are not anagrams")
