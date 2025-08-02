

import requests

paper_url = "http://old.mu.ac.in/wp-content/uploads/2014/11/1T040111.pdf"
res = requests.get(paper_url)
print(res)

with open("mepaper.pdf", "wb") as f:
	f.write(res.content)
	print("paper downloaded")
