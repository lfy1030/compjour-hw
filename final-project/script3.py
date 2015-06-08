import sys
import os
import csv

fn = "cat21"
keyword = "Others"

header = ["Prefecture", "Name", "Location", "Cs-134", "Cs-134 MDA", "Cs-137", "Cs-137 MDA", "Date", "Time Measures (sec)", "Instrument", "Lab", "Cat 1", "Cat 2", "Cat 3"]
theCSV = csv.writer(open("temp.csv", "w", encoding='utf-8'))
theCSV.writerow(header)

path = os.path.expanduser("~/Documents/GitHub/compjour-hw/final-project/data_nashi.csv")
with open(path, 'r', encoding='utf-8') as f:
	reader = csv.reader(f)
	for row in reader:
		if(row[11] == keyword):
			theCSV.writerow(row)

f = open(fn+".csv", "w", encoding='utf-8')
f2 = open("temp.csv", "r", encoding='utf-8')
for line in f2:
	if(len(line)>1):
		f.write(line)
f.close()
