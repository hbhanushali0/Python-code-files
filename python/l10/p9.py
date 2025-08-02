# multi threading - wapp for oop threads

import threading
import time

class Writing(threading.Thread):
	def run(self):
		print("writing started  ")
		for i in range(1, 11):
			print("writing ", i, "assignment ")
			time.sleep(1)
		print("writing completed ")

class Music(threading.Thread):
	def run(self):
		print("music started ")
		for i in range(1, 11):
			print("listen", i, "song " )
			time.sleep(1)
		print("music over ")

print("Initiating Today's Work ")
w = Writing()
m = Music()
w.start()
m.start()
w.join()
m.join()
print("Today's Work Ended ")
