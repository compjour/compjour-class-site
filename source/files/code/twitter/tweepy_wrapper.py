import json
import os
import tweepy
DEFAULT_TWITTER_CREDS_PATH = '~/.twittercreds.json'

def get_twitter_client(path = DEFAULT_TWITTER_CREDS_PATH):
    """
    returns: a Tweepy API object
    """
    full_creds_path = os.path.expanduser(path)
    creds = json.load(open(full_creds_path))
    auth = tweepy.OAuthHandler(consumer_key = creds['consumer_key'],
        consumer_secret = creds['consumer_secret'])
    auth.set_access_token(creds['access_token'],
      creds['access_token_secret'])

    return tweepy.API(auth)

def get_full_user_timeline(screen_name, api = None):
    if api is None:
        api = get_twitter_client()
    tweets = []
    cursor = tweepy.Cursor(api.user_timeline, id = screen_name,
      trim_user = True, exclude_replies = False, include_rts = True)
    for tweet in cursor.items():
        tweets.append(tweet._json)

    return tweets

