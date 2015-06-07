import urllib.request
import requests
import os
import sys
import csv

#First layer
path = "http://www2.census.gov/govs/statetax/14staxcd.txt"
#response = requests.get(path)
#soup = BeautifulSoup(response.text)
fn = "taxstates.csv"
urllib.request.urlretrieve(path, fn)
path = os.path.expanduser("~/Documents/GitHub/compjour-hw/SSS/" + fn)

with open(path, 'r') as f:
    reader = csv.reader(f)
    counter = 0
    for row in reader:
    	counter += 1
    	if(counter == 2):
        	print("$" + row[5][5:15])