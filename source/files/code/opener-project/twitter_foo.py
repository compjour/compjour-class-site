import json
import csv
import os.path
from glob import glob
from datetime import datetime
from operator import itemgetter
DATA_DIR = 'data-hold'
PROFILES_DIR = os.path.join(DATA_DIR, 'profiles')
TWEETS_DIR = os.path.join(DATA_DIR, 'tweets')


def get_ca_tweeters():
    csvname = os.path.join(DATA_DIR, 'sunlight_legislators.csv')
    csvdata = csv.DictReader(open(csvname, encoding = 'utf-8'))
    members = []
    for row in csvdata:
        if row['in_office'] == '1' and row['state'] == 'CA' and row['twitter_id'] != '':
            members.append(row)

    return members


def get_profile(screen_name):
    pfname = os.path.join(PROFILES_DIR, screen_name + '.json')
    profile = json.loads(open(pfname, encoding = 'utf-8').read())

    return profile


def get_tweets(screen_name):
    tfname = os.path.join(TWEETS_DIR, screen_name + '.json')
    tweets = json.loads(open(tfname, encoding = 'utf-8').read())

    return tweets


def get_original_tweets(screen_name):
    tweets = get_tweets(screen_name)
    original_tweets = [t for t in tweets if t.get('retweeted_status') == None]

    return original_tweets


def convert_twitter_timestamp(cstr):
    # cstr looks like: "Fri Oct 03 20:18:31 +0000 2008"
    return datetime.strptime(cstr, '%a %b %d %H:%M:%S +0000 %Y')


def get_tweets_with_word(screen_name, some_word):
    word = some_word.lower()
    orgtweets = get_original_tweets(screen_name)
    xlist = []
    for tweet in orgtweets:
        if word in tweet['text'].lower():
            xlist.append(tweet)

    return xlist
