# wapp to count occurrences of each letter
# i/p - kamall
# o/p - k - 1  a - 2  m - 1  l - 2

s1 = input("enter a string ")

count_letter = {}

for s in s1:
	ans = count_letter.get(s, -1) 
	if ans == -1:
		count_letter[s] = 1
	else:
		count_letter[s] = ans + 1
print(count_letter )	

		