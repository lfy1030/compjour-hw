
import bs4
import requests
import re

response = requests.get('http://www.justice.gov/feeds/opa/justice-news.xml')
soup = bs4.BeautifulSoup(response.text)
items = soup.findAll("item")
counter = 0
for i in items:
	search_str = str(i)
	matchObj = re.search( r'<pubdate>(.*?)</pubdate>', search_str, re.M|re.I)
	result = matchObj.group(1)
	if "2015-06-05" in result:
		counter += 1

print(counter)