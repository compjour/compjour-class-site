from twip import twitter_client

def make_it_so(tweet):
    resp = twitter_client().retweet(id = tweet.id)
    return resp
