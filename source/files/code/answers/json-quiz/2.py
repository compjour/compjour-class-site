import requests
import json
data_url = "http://www.compjour.org/files/code/json-examples/graph.facebook-whitehouse.json"
response = requests.get(data_url)
data = json.loads(response.text)

print('A.', data['checkins'])
print('B.', data['likes'])
print('C.', data['location']['longitude'])
print('D.', data['category_list'][-1]['name'])
