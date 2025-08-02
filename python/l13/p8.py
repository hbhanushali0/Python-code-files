


import bs4
import requests

try:
	res = requests.get("http://www.brainyquote.com/quotes_of_the_day.html")
	print(res)
	soup = bs4.BeautifulSoup(res.text, 'lxml')

	quote = soup.find('img', {"class": "p-qotd"})
	print(quote)

	photo_url = "http://www.brainyquote.com/" + quote['data-img-url']
	res = requests.get(photo_url)
	import datetime
	date = datetime.datetime.now().date()
	file_name = str(date) + ".jpeg"
	with open(file_name, "wb") as f:
		f.write(res.content)


	msg = quote['alt']
	print("message of the day ", msg)

except Exception as e:
	print("issue", e)
