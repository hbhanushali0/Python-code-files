

import bs4
import requests

res = requests.get("http://www.brainyquote.com/quotes_of_the_day.html")
print(res)
soup = bs4.BeautifulSoup(res.text, 'lxml')

quote = soup.find('img', {"class": "p-qotd"})
print(quote)

msg = quote['alt']
print("message of the day ", msg)



