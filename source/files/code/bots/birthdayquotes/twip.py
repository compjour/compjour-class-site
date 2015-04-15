import tweepy
import json
from os.path import expanduser
DEFAULT_CREDS_FILE = '~/.creds/raisenotbeg.json'

# """
# Expects {credsfile} to be a filename for a JSON file in this format:
# {
#   "consumer_key": "XXXXX",
#   "consumer_secret": "YYYYYY",
#   "access_token": "ZZZZZZ",
#   "access_token_secret": "AAAAAAA"
# }
# Returns an authenticated tweepy.API object
# """
def twitter_client(credsfile = None):

    fn = DEFAULT_CREDS_FILE if credsfile is None else credsfile
    ffn = expanduser(fn)  # get the full path in case the ~ is used
    c = json.load(open(ffn))
    # Get authentication token
    auth = tweepy.OAuthHandler(consumer_key = c['consumer_key'],
                               consumer_secret = c['consumer_secret'])
    auth.set_access_token(c['access_token'], c['access_token_secret'])
    # create an API handler
    return tweepy.API(auth)
