import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
countries = ['China', 'South Africa', 'Tajikistan']
total_jobs = 0
for c in countries:
    atts = {'Country': c,  'NumberOfJobs': 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    data = resp.json()
    num_jobs = int(data['TotalJobs'])
    print("%s currently has %s job listings.." % (c, num_jobs))
    total_jobs += num_jobs
print("Together, they have %s total job listings." % total_jobs)

        