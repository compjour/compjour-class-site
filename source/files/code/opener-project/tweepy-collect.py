
import json
import os
import tweepy
import csv
from io import StringIO
import requests

os.makedirs('data-hold/tweets', exist_ok = True)
os.makedirs('data-hold/profiles', exist_ok = True)


# First, authenticate with Twitter
credsfile = os.path.expanduser('~/.tweepyrc')
creds = json.load(open(credsfile))
# Get authentication token
auth = tweepy.OAuthHandler(consumer_key = creds['consumer_key'],
  consumer_secret = creds['consumer_secret'])
auth.set_access_token(creds['access_token'],
  creds['access_token_secret'])

# create an API handler
api = tweepy.API(auth)




# First, download the CSV from Sunlight
# Landing page is here:
# https://sunlightlabs.github.io/congress/#legislator-spreadsheet
print("Downloading legislators.csv")
sunlight_csv_url = 'http://unitedstates.sunlightfoundation.com/legislators/legislators.csv'
sundata = requests.get(sunlight_csv_url).text
# save it to disk
with open("data-hold/sunlight_legislators.csv", "w", encoding = 'utf-8') as o:
    o.write(sundata)
# now convert the data into a Dict
legislators = csv.DictReader(StringIO(sundata))
for x in legislators:
    # only collect data for sitting California Congressmembers with twitter accounts
    if x['state'] == 'CA' and x['in_office'] == '1' and x['twitter_id'] != '':
        twitter_id = x['twitter_id'].lower()
        # Now we talk to the Twitter API
        # first we get the profile
        print("Getting profile for", twitter_id)
        profile = api.get_user(twitter_id)
        with open('data-hold/profiles/{}.json'.format(twitter_id), "w", encoding = 'utf-8') as jfile:
            jtext = json.dumps(profile._json, indent = 2)
            jfile.write(jtext)

        # Now we get the tweets
        print("Getting tweets for", twitter_id)
        tweets = api.user_timeline(twitter_id,
                    trim_user = True, count = 200,
                    exclude_replies = False, include_rts = True)
        with open('data-hold/tweets/{}.json'.format(twitter_id), "w", encoding = 'utf-8') as jfile:
            jtext = json.dumps([t._json for t in tweets], indent = 2)
            jfile.write(jtext)



### zip it up
import shutil
shutil.make_archive("sunlight-twitter-opener", 'zip', "data-hold/")
