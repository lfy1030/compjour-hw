#script used to download each of the html files from the prefectures

import urllib.request
from bs4 import BeautifulSoup
import requests
import os
import sys

#First layer
path = "https://inventory.data.gov/dataset/fe9eeb10-2e90-433e-a955-5c679f682502/resource/b626ef1f-9019-41c4-91aa-5ae3f7457328/download/federalexecagncyintntdomains03302015.csv"
#response = requests.get(path)
#soup = BeautifulSoup(response.text)
fn = "domains.csv"
urllib.request.urlretrieve(path, fn)

path = os.path.expanduser("~/Documents/GitHub/compjour-hw/SSS/" + fn)
with open(path, "r") as myfile:
    count = sum(1 for line in myfile)
#for the header row
print(count-1)
