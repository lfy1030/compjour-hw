import json
import requests
import os
from collections import Counter
from operator import itemgetter

with open("sample-geochart-cities.html") as f:
    htmlstr = f.read()
CA_FILE = 'data-hold/california.json'
if not os.path.exists(CA_FILE):
    print("Can't find", CA_FILE, "so fetching remote copy")
    resp = requests.get("http://stash.compjour.org/data/usajobs/california-all.json")
    f = open(CA_FILE, 'w')
    f.write(resp.text)
    f.close()
rawdata = open(CA_FILE).read()
jdata = json.loads(rawdata)
jobs = jdata['jobs']

def extract_location(locations):
	buffer1 = locations.split(';')
	buffer_list = []
	for b in buffer1:
		buffer2 = b.split(',')
		if(len(buffer2) > 1):
			if 'Cali' in buffer2[1]:
				buffer_list.append(buffer2[0])
	return buffer_list

raw_list = []
for job in jobs:
	loc = extract_location(job['Locations'])
	if(len(loc) > 0):
		for l in loc:
			raw_list.append(l)

c = Counter(raw_list)

list_data = []
for c, j in dict(c).items():
	list_data.append([c, j])

list_data = sorted(list_data, key = itemgetter(1), reverse = True)

chartdata = [['City', 'Jobs']]
chartdata.extend(list_data)

tablerows = []
for d in list_data:
    tablerows.append("<tr><td>%s</td><td>%s</td></tr>" % (d[0], d[1]))

tablerows = "\n".join(tablerows)
#
with open("2-15.html", "w") as f:
    htmlstr = htmlstr.replace('#CHART_DATA#', str(chartdata))
    htmlstr = htmlstr.replace('#TABLE_ROWS#', tablerows)
    f.write(htmlstr)