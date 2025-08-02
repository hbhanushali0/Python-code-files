# wapf myrange() to which we can pass 1 arg and 2 arg
# e.g. myrange(5) - print ==> 1 2 3 4 5 
# myrange(2,6) - print ==> 2 3 4 5 6 

def myrange(p1=None, p2=None):
	if p1 is not None and p2 is None:
		start = 1
		while start <= p1:
			print(start)
			start = start + 1
	if p1 is not None and p2 is not None:
		start = p1
		while start <= p2:
			print(start)
			start = start + 1
myrange(3,9)
