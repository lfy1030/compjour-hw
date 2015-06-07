import urllib.request
import requests
import os
import sys
import csv


path = "https://www.osha.gov/dep/fatcat/fy15_federal-state_summaries.csv"
fn = "fatalities.csv"
urllib.request.urlretrieve(path, fn)
p = os.path.expanduser("~/Documents/GitHub/compjour-hw/SSS/" + fn)

with open(p, 'r') as f:
    reader = csv.reader(f)
    counter = 0
    for row in reader:
    	if(row[4] == "Fatality"):
    		counter += 1

print(counter)