import urllib.request
import requests
import os
import sys
import csv

fn = "enplanements.csv"
path = os.path.expanduser("~/Documents/GitHub/compjour-hw/SSS/" + fn)

with open(path, 'r') as f:
    reader = csv.reader(f)
    counter = 0
    for row in reader:
    	if(counter == 1):
    		print(row[8])
    	counter+=1