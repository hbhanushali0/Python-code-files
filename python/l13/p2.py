

import socket
import requests

try:
	socket.create_connection(("www.google.com", 80))
	print("u r connected")
	res = requests.get("https://ipinfo.io")
	print(res)
	data = res.json()
	print(data)
	city = data['city']
	print("city name ", city)
	loc = data['loc']
	latlon = loc.split(",")
	lat = latlon[0]
	lon = latlon[1]
	print("latitude", lat)
	print("longitude", lon)

except OSError as e:
	print("check network", e)


