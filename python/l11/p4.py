# wapp to wish user good morning/afternoon/evening and also display date and time

import datetime

dt = datetime.datetime.now()

date = dt.date()
print("date = ", date)

time = dt.time()
print("time = ", time)
s1 = time.strftime('%I:%M:%S %p')
print(s1)

hour = dt.hour
msg = " "

if hour >= 6 and hour < 12:
	print("Good Morning ")

elif hour >= 12 and hour < 17:
	print("Good Afternoon")

else:
	msg = "Good Evening"

print(msg)

