# wapp to race condition solution using semaphore


import threading
import time

balance = 500
s = threading.Semaphore()

def deposit():
	print("deposit process started ")
	s.acquire()
	global balance
	amt1 = balance
	amt1 = amt1 + 100
	time.sleep(2)
	balance = amt1
	s.release()
	print("deposit process ended ")


def withdraw():
	print("withdraw process started ")
	global balance
	s.acquire()
	amt2 = balance
	amt2 = amt2 - 100
	time.sleep(2)
	balance = amt2
	s.release()
	print("withdraw process ended ")

print("initial balance ", balance)
t1 = threading.Thread(target = deposit)
t2 = threading.Thread(target = withdraw)
t1.start()
t2.start()
t1.join()
t2.join()
print("final balance ", balance)
