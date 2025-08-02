# wapp for threading using pop approach

import threading
import time

def writing():
	print("writing started  ")
	for i in range(1, 11):
		print("writing ", i, "assignment ")
		time.sleep(1)
	print("writing completed ")

def music():
	print("music started ")
	for i in range(1, 11):
		print("listen", i, "song " )
		time.sleep(1)
	print("music over ")

print("Initiating Today's Work ")
w = threading.Thread(target = writing)
m = threading.Thread(target = music)
w.start()
m.start()
w.join()
m.join()
print("Today's Work Ended ")
