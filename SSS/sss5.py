import requests
import json
data_url = "https://data.consumerfinance.gov/resource/x94z-ydhh.json"
# fetch the data file
response = requests.get(data_url)
text = response.text
# parse the data
data = json.loads(text)

student_loans = []

for a in data:
	if(a['product'] == "Student loan"):
		student_loans.append(a)

print(student_loans[0]['company'])
