# wapp to read n marks from user and find the following:

# 1) avg marks	2) highest marks	3) lowest marks

# 4) count no >= 70	5) count no <= 40 


import array

marks = array.array('i', [])

num = int(input("please enter number of students"))

for i in range(num):
	m = int(input("please enter marks"))
	marks.append(m)

sum = 0
for m in marks:
	sum = sum + m


avg = sum / num
print("average = ", avg)

high = low = marks[0]
for m in marks:
	if m > high:
		high = m
	if m < low:
		low = m

print("highest marks = ", high)
print("lowest marks = ",low)

no70, no40 = 0, 0

for m in marks:
	if m >= 70:
		no70 = no70 + 1
	if m >= 40:
		no40 = no40 + 1
print("70= ", no70)
print("40= ", no40)