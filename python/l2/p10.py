# wapp to read marks and display grades

marks = int(input("please enter your marks"))

if marks >= 70:
	grade=("distinction")
elif marks >= 60:
	grade=("First Class")
elif marks >= 50:
	grade=("Second Class")
elif marks >= 40:
	grade=("Third Class")
else:
	grade =("fail")
print(" your grade is ", grade)
