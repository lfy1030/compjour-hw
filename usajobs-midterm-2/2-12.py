import json
import requests
import os
## for subsequent exercises
## copy this data-loading snippet
CA_FILE = 'data-hold/california.json'
if not os.path.exists(CA_FILE):
    print("Can't find", CA_FILE, "so fetching remote copy...")
    resp = requests.get("http://stash.compjour.org/data/usajobs/california-all.json")
    f = open(CA_FILE, 'w')
    f.write(resp.text)
    f.close()
rawdata = open(CA_FILE).read()
jobs = json.loads(rawdata)['jobs']
## end data-loading code


# val is a string that looks like "$45,000"
# the return value is a Float: 45000.00
def cleanmoney(val):
    x = val.replace('$', '').replace(',', '')
    return float(x)

# job is  Dictionary object;  perform the cleanmoney() function on the
#  'SalaryMax' value and return it
def cleansalarydiff(job):
    return cleanmoney(job['SalaryMax'])-cleanmoney(job['SalaryMin'])

filteredjobs = []
for j in jobs:
	if(cleanmoney(j['SalaryMax'])<100000):
		filteredjobs.append(j)

# sort the jobs list based on the result of cleansalarydiff
filteredjobs = sorted(jobs, key = cleansalarydiff, reverse = True)

job = filteredjobs[0]
print('%s,%d,%d' % (job['JobTitle'], cleanmoney(job['SalaryMin']), cleanmoney(job['SalaryMax'])))


