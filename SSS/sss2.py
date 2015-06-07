import bs4
import requests
response = requests.get('http://catalog.data.gov/dataset?q=&sort=metadata_created+desc&ext_location=&ext_bbox=&ext_prev_extent=-139.21874999999997%2C8.754794702435605%2C-61.87499999999999%2C61.77312286453148')
soup = bs4.BeautifulSoup(response.text)
print(soup.h3.a.text)
