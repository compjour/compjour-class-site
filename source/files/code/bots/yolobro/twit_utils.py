import os.path
import json
import tweepy
from copy import copy
def get_api(credsfile):
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



def normalize_tweepy_data(td):
    """
    A helper function that converts Tweepy data objects into standard
    dicts and lists

    Arguments:
      - td (some kind of object)

    Returns:
      - either a dict or a list
    """
    if issubclass(type(td), list):
        return [d._json if hasattr(d, '_json') else d for d in td ]
    else:
        return td._json if hasattr(td, '_json') else td




def tweet(credsfile, txt, opts = {}):
    """
    Sends out a tweet on behalf of the user authenticated via `credsfile`

    Arguments:
      - credsfile (str): the full path of the filename that contains a JSON
        file with credentials for Twitter
      - txt (str): a string of text for the body of the tweet
      - opts (dict, optional): a set of options to pass to the Tweepy client,
            e.g. in_reply_to_status_id, media_ids
            as defined at: https://dev.twitter.com/rest/reference/post/statuses/update

    Examples:
        - Send a simple tweet:
           tweet("~/.mycreds", "Whats up")

        - Send a tweet and tell Twitter to hide it from safe-searching users
           tweet("~/.mycreds", "Gettin wild!, {'possibly_sensitive': True})

    Returns:
        A dict. If there are no errors on Twitter's side, the data representation
         of the sent tweet is returned

    """
    options = copy(opts)
    options['status'] = txt
    api = get_api(credsfile)
    resp = api.update_status(**options)

    return normalize_tweepy_data(resp)



def reply(credsfile, txt, reply_to_tweet, opts = {}):
    """
    Sends out a reply on behalf of the user authenticated via `credsfile`, to the
    user who authored `tweet`

    Arguments:
      - credsfile (str): the full path of the filename that contains a JSON
        file with credentials for Twitter
      - txt (str): a string of text for the body of the reply
      - reply_to_tweet (dict): the data for a single Tweet, as received from Twitter's API.
        It should have a `user` attribute.
      - opts (dict, optional): a set of options to pass to the Tweepy client,
            e.g. media_ids
            as defined at: https://dev.twitter.com/rest/reference/post/statuses/update
    """
    options = copy(opts)
    options['in_reply_to_status_id'] = reply_to_tweet['id']
    tweeter_screenname = reply_to_tweet['user']['screen_name']
    options['status'] = "@%s %s" % (tweeter_screenname, txt)
    api = get_api(credsfile)
    resp = api.update_status(**options)
    return normalize_tweepy_data(resp)


def get_mentions(credsfile, opts = {}):
    options = copy(opts)
    options['count'] = options['count'] if options.get('count') else 50
    options['since_id'] = options['since_id'] if options.get('since_id') else 1
    options['trim_user'] = False
    api = get_api(credsfile)
    resp = api.mentions_timeline(**options)
    return normalize_tweepy_data(resp)

def get_latest_tweets_from_me(credsfile, opts = {}):
    options = copy(opts)
    options['count'] = options['count'] if options.get('count') else 50
    options['since_id'] = options['since_id'] if options.get('since_id') else 1
    options['trim_user'] = True
    options['exclude_replies'] = False
    api = get_api(credsfile)
    resp = api.user_timeline(**options)
    return normalize_tweepy_data(resp)

def get_latest_tweets_from_list(credsfile, owner_screen_name, slug, opts = {}):
    """
    Returns the a list of the latest Tweets (as dict objects) from
    the tweets created by list {owner_screen_name}/{slug}'s members
    """
    options = copy(opts)
    options['count'] = options['count'] if options.get('count') else 50
    options['since_id'] = options['since_id'] if options.get('since_id') else 1
    options['trim_user'] = False
    options['owner_screen_name'] = owner_screen_name
    options['slug'] = slug
    api = get_api(credsfile)
    resp = api.list_timeline(**options)

    return normalize_tweepy_data(resp)




def get_latest_tweets(credsfile, q, opts = {}):
    options = copy(opts)
    options['count'] = options['count'] if options.get('count') else 50
    options['since_id'] = options['since_id'] if options.get('since_id') else 1
    options['trim_user'] = False
    options['result_type'] = options['result_type'] if options.get('result_type') else 'recent'
    api = get_api(credsfile)
    resp = api.search(q = q, **options)

    return normalize_tweepy_data(resp)





