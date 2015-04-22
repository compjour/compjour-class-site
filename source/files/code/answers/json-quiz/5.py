import requests
import json
data_url = 'http://www.compjour.org/files/code/json-examples/single-tweet-librarycongress.json'
data = json.loads(requests.get(data_url).text)

print('A.', data['created_at'])
print('B.', data['user']['created_at'])
print('C.', data['text'])
print('D.', data['user']['screen_name'])
print('E.', data['id'])
print('F.', len(data['entities']['user_mentions']))

### For G.
hashtag_objs = data['entities']['hashtags']
hashtag_texts = []
for h in hashtag_objs:
    hashtag_texts.append(h['text'])
print('G.', ','.join(hashtag_texts))
# alternatively, you could also use the list comprehension syntax:
# hashtag_texts = [h['text'] for h in data['entities']['hashtags']]


### For H
urls = data['entities']['urls']
urltxts = []
for u in urls:
    urltxts.append(u['display_url'])
print('G.', ','.join(urltxts))
