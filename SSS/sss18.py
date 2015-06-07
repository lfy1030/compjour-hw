import requests
import os
import sys
import csv

fn = "legislators.csv"
path = os.path.expanduser("~/Documents/GitHub/compjour-hw/SSS/" + fn)

data = csv.DictReader(open("legislators.csv"))
rows = list(data)
counter = 0
for r in rows:
	if(r['gender'] == "F" and r['in_office'] == '1'):
		counter += 1
print(counter)