import json
import requests
import os
from datetime import datetime
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

collection_date = datetime.strptime(jdata['date_collected'], '%Y-%m-%dT%H:%M:%S')

## end job-loading code

def cleanmoney(val):
    x = val.replace('$', '').replace(',', '')
    return float(x)

def daysleft(job):
    lastdate = datetime.strptime(job['EndDate'], '%m/%d/%Y')
    return (lastdate - collection_date ).days

filtered_jobs = []
for job in jobs:
    if(cleanmoney(job['SalaryMin']) >= 90000):
        filtered_jobs.append(job)

for job in sorted(filtered_jobs, key = daysleft):
    days = daysleft(job)
    if days < 5 and days >= 0:
        print('%s,%s,%s' % (job['JobTitle'], days, job['ApplyOnlineURL']))

        