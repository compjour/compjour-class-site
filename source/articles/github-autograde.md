---
title: How to Auto-Grade People on Github
---

Having fun with Github

(note: if your repo is set to private, you [will have to go through the authentication process](https://developer.github.com/v3/auth/))

* TOC
{:toc .tock}

## Github API docs

[developer.github.com/v3/](https://developer.github.com/v3/)


The base endpoint is: `https://api.github.com`

To get a [single user's data](https://developer.github.com/v3/users/) (in this case, the user [blahs555](https://github.com/blahs555):

[https://api.github.com/users/blahs555](https://api.github.com/users/blahs555)

If you [visit that URL](https://api.github.com/users/blahs555), you'll see it returns a JSON file that helpfully lists all the other endpoints.

To get a list of that user's repos:

[https://api.github.com/users/blahs555/repos](https://api.github.com/users/blahs555/repos)


### User events endpoints 

Or even the [list of the user's latest activity](https://developer.github.com/v3/activity/events/) (handy for calculating if you've been committing to Github on a regular basis):

[https://api.github.com/users/blahs555/events](https://api.github.com/users/blahs555/events)


#### Get a list of last 100 events:

~~~py
import requests
from datetime import datetime
username = 'blahs555'
url = 'https://api.github.com/users/%s/events?per_page=100' % username
eventdata = requests.get(url).json()
mylist = []
for event in eventdata:
    d = {}
    d['type'] = event['type'] 
    d['repo'] = event['repo']['name']
    d['url'] = event['repo']['url']
    d['timestamp'] = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ')
    d['days_ago'] = (datetime.now() - d['timestamp']).days
    if event['payload'].get('commits'):
        d['messages'] = ', '.join([ev.get('message') for ev in event['payload']['commits']])
    else:
        d['messages'] = ""

  
    mylist.append(d)


print("\t".join(['type', 'repo', 'days_ago', 'messages']))
for event in mylist:
    print("\t".join([event['type'], event['repo'], str(event['days_ago']), event['messages']]))
~~~



### How to grade like a bot

But I don't even really need to know the API if all I need to know is: _does user X have file Z inside of their repo Y?_


For example, if I expect user `blahs555` to have a file named `json-quiz/1.py` inside of their `compjour-hw` repo, this is the direct URL which I can visit via web browser:


[https://github.com/blahs555/compjour-hw/blob/master/json-quiz/1.py](https://github.com/blahs555/compjour-hw/blob/master/json-quiz/1.py)


And with Python, maybe the first thing I check is whether a file even exists:

~~~py
import requests
url = 'https://github.com/blahs555/compjour-hw/blob/master/json-quiz/1.py'
resp = requests.get(url)
if resp.status_code == 200:
  print("Nice job!")
else: 
  print("BAD!")
~~~


And so if I have a list of files/folders that I *know* should exist, then here's an easy auto-grader:

(one key takeaway: notice how if you have any kind of typo in the filename, my grading bot will assume the homework wasn't done. Think about it...)

~~~py
import requests
REPO_NAME = 'compjour-hw'
BASEURL = 'https://github.com/%s/compjour-hw/blob/master/%s'
FILES = [
  'json-quiz',
  'opener-project',
  'twitterbot',
  'usajobs-midterm-1'
]


def is_assignment_done(url):      
      resp = requests.head(url)
      return resp.status_code == 200 or resp.status_code == 301


def is_passing(username):
    fails = 0
    for f in FILES:
        url = BASEURL % (username, f)
        if is_assignment_done(url) == False:
            print("    FAILED:", f)
            fails += 1
    return fails == 0


for username in ['blahs555', 'dannguyen', 'Stanford']:
    print("Testing user", username)
    x = is_passing(username)
    if x:
        print("  * A:", username)
    else:
        print("  * F:", username)
~~~
