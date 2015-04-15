import requests
import json
data_url = "http://www.compjour.org/files/code/json-examples/spotify-related-to-beyonce.json"
data = json.loads(requests.get(data_url).text)

artist_obj = data['artists']
print('A.', len(data['artists']))
print('B', artist_obj[4]['name'])
print('C', artist_obj[11]['followers']['total'])
print('D', ', '.join(artist_obj[0]['genres']))
print('E', artist_obj[19]['images'][0]['url'])