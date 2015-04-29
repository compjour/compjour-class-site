import requests
import json
import os
data_url = 'http://www.compjour.org/files/code/json-examples/twitter-cspan-congress-list.json'
tempfilename = "/tmp/congresslist.json"
# if you're on Windows, do this:
# tempfilename = os.path.expandvars('%TEMP%\\congresslist.json')

# Because this file is relatively large, let's save it to a tempfile, so that
# subsequent runs read from that file
if os.path.exists(tempfilename):
    tfile = open(tempfilename, "r")
    j = tfile.read()
else:
    j = requests.get(data_url).text
    tfile = open(tempfilename, "w")
    tfile.write(j)

tfile.close()
accounts = json.loads(j)
## woof, that was a lot of lines just to load a file...
##################################################

#############
## Task A:
print('A.', len(accounts))

#############
## Task B:
x = 0
for a in accounts:
    if a['followers_count'] > 10000:
        x += 1

## or more concisely:
# x = len([a for a in accounts if a['followers_count'] > 10000])
print("B.", x)


#############
## Task C:
x = len([a for a in accounts if a['verified'] == True])
print("C.", x)


#############
## Task D:
counts = []
for a in accounts:
    counts.append(a['followers_count'])
maxval = sorted(counts, reverse = True)[0]
# alternatively:
# maxval = sorted([a['followers_count'] for a in accounts], reverse = True)[0]

## or:
# counts = []
# for a in accounts:
#    counts.append(a['followers_count'])
# maxval = max(counts)

## or:
# maxval = max(a['followers_count'] for a in accounts)
print("D.", maxval)


###############
## Task E:
print("E.", max(a['statuses_count'] for a in accounts))


##############
## Task F:
from operator import itemgetter
y = sorted(accounts, key = itemgetter('followers_count'), reverse = True)
x = y[0]
# alternatively:
# x = max(accounts, key = itemgetter('followers_count'))
print("F.", x['screen_name'], 'has', x['followers_count'], 'followers')

##############
## Task G:
from operator import itemgetter
vaccs = sorted(accounts, key = itemgetter('statuses_count'), reverse = True)
accs = [a for a in vaccs if a['verified'] == False]
x = accs[0]
print("G.", x['screen_name'], 'has', x['statuses_count'], 'tweets')


###############
## Task H:
totes = 0
for a in accounts:
    totes += a['followers_count']

# alternatively
# totes = sum([a['followers_count'] for a in accounts])
print('H.', round(totes / len(accounts)))


###############
## Task I:
from operator import itemgetter
z = sorted(accounts, key = itemgetter('followers_count'))
m = z[len(z) // 2]
print("I.", m['followers_count'])
