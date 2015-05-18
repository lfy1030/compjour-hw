import json
import os
import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
CODES_URL = "http://stash.compjour.org/data/usajobs/us-statecodes.json"
cdata = requests.get(CODES_URL).json()
mylist = []
for s in cdata.items():
    print("Getting:", s[0])
    atts = {'Countrysubdivision': s[0],  'NumberOfJobs': 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    data = resp.json()
    jobcount = int(data['TotalJobs'])
    mylist.append([s[0], jobcount])

# save the file on to your hard drive
os.makedirs("data-hold", exist_ok = True)
f = open("data-hold/domestic-jobcount.json", 'w')
f.write(json.dumps(mylist, indent = 2))
f.close()
