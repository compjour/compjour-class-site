import requests
import json
data_url = "http://www.compjour.org/files/code/json-examples/maps.googleapis-geocode-mcclatchy.json"
response = requests.get(data_url)
data = json.loads(response.text)

obj = data['results'][0]
print('A.', obj['formatted_address'])
print('B.', data['status'])
print('C.', obj['geometry']['location_type'])
print('D.', obj['geometry']['location']['lat'])
print('E.', obj['geometry']['viewport']['southwest']['lng'])

a = obj['address_components'][0]['long_name']
b = obj['address_components'][1]['long_name']
print('F.', a + ', ' + b)
# or, to use list comprehensions:
# print('F.', ', '.join(a['long_name'] for a in obj['address_components'][0:2]))
