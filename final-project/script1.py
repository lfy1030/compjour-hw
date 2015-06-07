#script used to download each of the html files from the prefectures

import urllib.request
import bs4
import requests
import re

#First layer
path = "http://en.minnanods.net/mrdatafoodloc/"
response = requests.get('http://en.minnanods.net/mrdatafoodloc/')
soup = bs4.BeautifulSoup(response.text)
table = soup.find_all("tr")
for t in table:
    fn = str(t.td)
    fn_fixed = fn[4:len(fn)-5]
    if(len(fn_fixed) > 0):
        url = str(t.a)
        matchObj = re.match( r'<a href="(.*?)">.*', url, re.M|re.I)
        ubase = matchObj.group(1)
        fname = fn_fixed + '.html'
        print("Now printing..." + fname)
        print(path + ubase)
        urllib.request.urlretrieve(path+ubase, fname)