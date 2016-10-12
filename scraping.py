import requests
from bs4 import BeautifulSoup

url = "http://www.yellowpages.com/search?search_terms=cofee&geo_location_terms=Los+Angeles%2C+CA"  # put your desired web-address
r = requests.get(url);

print(r.content)

soup = BeautifulSoup(r.content)
print(soup)

links = soup.find_all("a")

for link in links:
	print(link.get("href"))

for link in links:
	print(link.text)

for link in links:
	print(link.text, link.get("href"))

for link in links:
	print("<a href='%s'>%s</a>" % (link.get("href"), link.text))

g_data = soup.find_all("div", {"class": "info"})
print(g_data)

for item in g_data:
	print(item.text)

for item in g_data:
	print(item.contents[0].text)
	print(item.contents[1].text)

for item in g_data:
	print(item.contents[0].find_all("a", {"class": "business-name"})[0].text)
	print(item.contents[1].find_all("p", {"class": "adr"})[0].text)
	try:
		print(item.contents[1].find_all("div", {"class": "primary"})[0].text)
	except:
		pass
