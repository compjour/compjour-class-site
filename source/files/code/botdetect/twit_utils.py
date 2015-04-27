from datetime import datetime
import time
import tweepy
import os
import json

DEFAULT_TWITTER_CREDS_PATH = '~/.creds/me.json'

def get_api(credsfile = DEFAULT_TWITTER_CREDS_PATH):
    """
    Takes care of the Twitter OAuth authentication process and
    creates an API-handler to execute commands on Twitter

    Arguments:
      - credsfile (str): the full path of the filename that contains a JSON
        file with credentials for Twitter

    Returns:
      A tweepy.api.API object

    """
    fn = os.path.expanduser(credsfile)  # get the full path in case the ~ is used
    c = json.load(open(fn))
    # Get authentication token
    auth = tweepy.OAuthHandler(consumer_key = c['consumer_key'],
                               consumer_secret = c['consumer_secret'])
    auth.set_access_token(c['access_token'], c['access_token_secret'])
    # create an API handler
    return tweepy.API(auth)




def convert_twitter_timestamp(t):
    """
    t is something like 'Sat Jan 30 03:36:19 +0000 2010'
    return: a datetime object
    """

    return datetime.fromtimestamp(time.mktime(time.strptime(t, '%a %b %d %H:%M:%S +0000 %Y')))


def get_user_recent_tweets(screen_name):
    options = {}
    options['count'] = 200
    options['since_id'] = 1
    options['trim_user'] = True
    options['exclude_replies'] = False
    options['include_rts'] = True
    api = get_api()
    tweets = api.user_timeline(**options)
    return [t._json for t in tweets]



def get_user_profile(screen_name):
    api = get_api()
    users = api.lookup_users(screen_names = [screen_name])
    # lookup_users always returns array
    profile = users[0]
    return profile._json


def get_user_followers_sample(screen_name):
    api = get_api()
    ids = api.followers_ids(screen_name, count = 5000)
    users = api.lookup_users(user_ids = ids[-101:-1])

    return [user._json for user in users]



def get_user(screen_name):
    """
    A convenience method
    Returns a dictionary:
    {
        'profile': the result of get_user_profile(screen_name),
        'tweets': the result of get_user_recent_tweets(screen_name),
        'followers': the result of get_user_followers_sample(screen_name)
    }
    """
    api = get_api()
    user = {}
    user['profile'] = get_user_profile(screen_name)
    user['tweets'] = get_user_recent_tweets(screen_name)
    user['followers'] = get_user_followers_sample(screen_name)

    return user
