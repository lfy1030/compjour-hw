import requests
from collections import Counter
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
resp = requests.get(BASE_USAJOBS_URL, params = {"CountrySubdivision": 'California', 'NumberOfJobs': 250})
data = resp.json()

org_names_list = []
for job in data['JobData']:
    org_names_list.append(job['OrganizationName'])

c = Counter(org_names_list)
print(dict(c))
