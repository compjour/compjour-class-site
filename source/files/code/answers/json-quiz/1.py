import requests
import json
data_url = "http://www.compjour.org/files/code/json-examples/analyticsgov-realtime.json"
# fetch the data file
response = requests.get(data_url)
text = response.text
# parse the data
data = json.loads(text)

print('A.', data['name'])
print('B.', data['taken_at'])
print('C.', data['meta']['name'])
print('D.', data['data'][0]['active_visitors'])
print('E.', ', '.join(data.keys()))
