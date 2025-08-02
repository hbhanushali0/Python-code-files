# wapp to read two set of student names:
# 1 android batch students
# 2 java batch students and display all names and common names

android = set()
java = set()

reply = input("do you want to add android student names yes/no  ")
while reply == "yes":
	n = input("please enter a name ")
	android.add(n)
	reply = input("do you want to add more names yes/no  ")

reply = input("do you want to add java student names yes/no  ")
while reply == "yes":
	n = input("please enter a name ")
	java.add(n)
	reply = input("do you want to add more names yes/no  ")

r1 = android | java
print("all students ", r1)
r2 = android & java
print("common students ", r2)
	