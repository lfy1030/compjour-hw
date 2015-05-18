import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
state_name = 'Alaska'
state_name2 = "Hawaii"
atts = {"CountrySubdivision": state_name, 'NumberOfJobs': 1}
resp = requests.get(BASE_USAJOBS_URL, params = atts)
data = resp.json()
num_jobs1 = data['TotalJobs']
print("%s has %s job listings." % (state_name, num_jobs1))
atts2 = {"CountrySubdivision": state_name2, 'NumberOfJobs': 1}
resp2 = requests.get(BASE_USAJOBS_URL, params = atts2)
data2 = resp2.json()
num_jobs2 = data2['TotalJobs']
print("%s has %s job listings." % (state_name2, num_jobs2))
total = int(num_jobs1) + int(num_jobs2)
print("Together, they have %s total job listings" % (total))