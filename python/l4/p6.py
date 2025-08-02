# wapp to count number of vowels and consonants present in string

s1 = input("enter a string")

vc,cc = 0,0

for s in s1:
	if s.isalpha():
		if s in ['a','e','I','o','u','A','E','I','O','U']:
			vc = vc + 1
		else:
			cc = cc + 1
print("vowels=",vc,"consonants=",cc)
