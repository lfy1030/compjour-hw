#This script is used to pull all the data into a single csv
import sys
import os
from bs4 import BeautifulSoup
import re
import csv

header = ["Prefecture", "Name", "Location", "Cs-134", "Cs-134 MDA", "Cs-137", "Cs-137 MDA", "Date", "Time Measures (sec)", "Instrument", "Lab", "Cat 1", "Cat 2", "Cat 3"]
theCSV = csv.writer(open("database.csv", "w", encoding='utf-8'))
theCSV.writerow(header)

path = os.path.expanduser("~/Documents/GitHub/compjour-hw/final-project/html")
#list containing all the files in this directory 
filenames = os.listdir(path)

for fn in filenames:
	pathname = path + "/" + fn
	soup = BeautifulSoup(open(pathname, "r", encoding='utf-8'))
	rows = soup.findAll("tr")
	pref_name = str(fn)[0:len(fn)-5]
	for row in rows:
		cols = row.findAll("td")
		counter = 0
		if(len(cols)>0):
			c_row = []
			c_row.append(pref_name)
			for c in cols:
				if(counter == 1):
					c_row.append(c.text)
				if(counter == 2):
					c_row.append(c.text)
				if(counter == 3):
					base = c.text
					matchObj = re.match( r'(.*?)\((.*?)\)', base, re.M|re.I)
					c_row.append(matchObj.group(1))
					c_row.append(matchObj.group(2))
				if(counter == 4):
					base2 = c.text
					matchObj = re.match( r'(.*?)\((.*?)\)', base2, re.M|re.I)
					c_row.append(matchObj.group(1))
					c_row.append(matchObj.group(2))
				if(counter == 5):
					c_row.append(c.text)
				if(counter == 6):
					c_row.append(c.text)
				if(counter == 7):
					c_row.append(c.text)
				if(counter == 8):
					base3 = c.text
					matchObj = re.search( r'(.*?)lab:(.*?)\n', base3, re.M|re.I)
					c_row.append(matchObj.group(2))
					matchObj2 = re.search( r'(.*?)category:(.*?)\n', base3, re.M|re.I)
					cat_str = matchObj2.group(2)
					matchObj3 = re.match( r'(.*?)>(.*?)>(.*)', cat_str, re.M|re.I )
					c_row.append(matchObj3.group(1))
					c_row.append(matchObj3.group(2))
					c_row.append(matchObj3.group(3))
				counter += 1
			theCSV.writerow(c_row)
			#print(c_row)

f = open("data.csv", "w", encoding='utf-8')
f2 = open("database.csv", "r", encoding='utf-8')
for line in f2:
	if(len(line)>1):
		f.write(line)
f.close()
