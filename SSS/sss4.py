import bs4
import requests
response = requests.get('https://www.usajobs.gov/Search?Keyword=librarian&Location=&search=Search&AutoCompleteSelected=False#')
soup = bs4.BeautifulSoup(response.text)
link = soup.select("span.pageset")[2]
print(link.text)