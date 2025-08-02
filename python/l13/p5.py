


import socket
import requests

try:
	socket.create_connection(("www.google.com", 80))
	mn = input("enter movie name")
	a1 = "http://www.omdbapi.com/?"
	a2 = "&apikey=b88add31"
	a3 = "&s=" + mn
	res = requests.get(a1 + a2 + a3)
	print(res)
	data = res.json()
	# print(data)
	info = data['Search']
	for i in info:
		print("*" * 50)
		print("movie name = ", i['Title'])
		print("year = ", i['Year'])
		print("poster = ", i['Poster'])

except OSError:
	print("check network")
