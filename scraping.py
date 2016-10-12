import requests
from bs4 import BeautifulSoup

url = "http://www.yellowpages.com/search?search_terms=cofee&geo_location_terms=Los%20Angeles%2C%20CA"
url2 = "http://www.yellowpages.com/search?search_terms=cofee&geo_location_terms=Los%20Angeles%2C%20CA&page=2"

def get_data_from_url(url, page):
	for i in range(page):
		u = url;
		if i > 0:
			u = url + ("&page=" + str(i+1))
			print(u)


r=r
get_data_from_url(url, 10);
print(r.content)

soup = BeautifulSoup(r.content, "html.parser")
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

result = 0
for item in g_data:
	print("----------------------------------------")
	print("----------------------------------------")
	print("Searching Result: " + str(result))
	result += 1

	try:
		print("Name: " + item.contents[0].find_all("a", {"class": "business-name"})[0].text)
	except:
		pass

	try:
		print("Address : " + item.contents[1].find_all("p", {"class": "adr"})[0].text)
	except:
		pass

	try:
		print("Street Address : " + item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text)
	except:
		pass

	try:
		print("Address Locality : " + item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text.replace(',', ''))
	except:
		pass

	try:
		print("Address Region : " + item.contents[1].find_all("span", {"itemprop": "addressRegion"})[0].text)
	except:
		pass

	try:
		print("Postal Code : " + item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text)
	except:
		pass

	try:
		print("Phone : " + item.contents[1].find_all("span", {"itemprop": "telephone"})[0].text)
	except:
		pass

	try:
		print("Categories : " + item.contents[2].find_all("a", {"class": "categories"})[0].text)
	except:
		pass






