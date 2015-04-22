import requests
import json
data_url = "http://www.compjour.org/files/code/json-examples/spotify-related-to-beyonce.json"
data = json.loads(requests.get(data_url).text)
artists = data['artists']

print('A.', len(artists))
print('B.', artists[4]['name'])
print('C.', artists[11]['followers']['total'])
print('D.', ','.join(artists[0]['genres']))
print('E.', artists[-1]['images'][0]['url'])

# Note: the answer to E depends on that images array being sorted by size
# ...if that weren't the case, we'd have to sort it like so:

# from operator import itemgetter
# images = sorted(artists[-1]['images'], key = itemgetter('width', 'height'))
# print('E.', images[-1]['url'])


