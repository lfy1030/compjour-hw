import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
states = ['California', 'Florida', 'Maryland', 'New York']
dictionary = {}
for s in states:
	atts = {'CountrySubdivision': s,  'NumberOfJobs': 1}
	resp = requests.get(BASE_USAJOBS_URL, params = atts)
	data = resp.json()
	dictionary[s] = int(data['TotalJobs'])

print(dictionary)