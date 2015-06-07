import requests
import os
import sys
import csv

fn = "wildlife.csv"
path = os.path.expanduser("~/Documents/GitHub/compjour-hw/SSS/" + fn)

with open(path, 'r') as f:
    reader = csv.reader(f)
    counter = 0
    for row in reader:
    	counter+=1

print(counter-1)