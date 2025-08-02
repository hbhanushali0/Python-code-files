

import socket
import requests
import matplotlib.pyplot as plt

city_name = ["Mumbai", "Dubai", "Singapore"]
city_temp = []
for c in city_name:
	try:
		socket.create_connection(("www.google.com", 80))
		a1 = "http://appi.openweathermap.org/data/2.5/weather?units=metric"
		a2 = "&q=" + c
		a3 = "&appid=f5bf5eb6ebd07c40fcef9d04720124b3"
		api_address = a1 + a2 + a3
		res1 = requests.get(api_address)
		print(res1)
		data = res1.json()
		temp1 = data['main']['temp']
		city_temp.append(temp1)
	
	except OSError as e:
		print("check network", e)

plt.bar(city_name, city_temp, width = 0.20)
plt.title("Weather Report")
plt.xlabel("City Names")
plt.ylabel("City Temp")
plt.grid()
plt.savefig("City.png")
plt.show()


