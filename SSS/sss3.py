import requests
import json
data_url = "https://analytics.usa.gov/data/live/ie.json"
# fetch the data file
response = requests.get(data_url)
text = response.text
# parse the data
data = json.loads(text)

print(data['totals']['visits'])