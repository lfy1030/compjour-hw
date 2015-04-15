import requests
import json
data_url = "http://www.compjour.org/files/code/json-examples/maps.googleapis-geocode-mcclatchy.json"
response = requests.get(data_url)
text = response.text
data = json.loads(text)

result_obj = data['results'][0]
print('A.',  result_obj['formatted_address'])
print('B', data['status'])
print('C.', result_obj['geometry']['location_type'])
print('D.', result_obj['geometry']['location']['lat'])
print('E.', result_obj['geometry']['viewport']['southwest']['lng'])
print('A.',  result_obj['address_components'][0]['long_name'], ',',result_obj['address_components'][1]['long_name'])
