import tweepy
import json
from os.path import expanduser
from random import randrange
from time import sleep

DEFAULT_CREDS_FILE = '~/.creds/raisenotbeg.json'
POSSIBLE_URLS = ['http://begthequestion.info/',
'http://en.wikipedia.org/wiki/Begging_the_question', 'http://www.qwantz.com/index.php?comic=693',
'http://afterdeadline.blogs.nytimes.com/2008/09/25/begging-the-question-again/?_r=0',
'http://ethics.npr.org/memos-from-memmott/listeners-are-begging-us-to-bag-begs-the-question/',
'http://www.npr.org/2014/11/15/364289503/so-what-bugs-listeners-about-nprs-grammar',
'http://www.lawprose.org/blog/?p=2864'
]
POSSIBLE_REPLIES = [
    "Pardon me, @{screen_name} but I believe you mean, 'raises the question' 🙌: {url}",
    "But is the question really being *begged*, @{screen_name}? {url}",
    "Maybe, @{screen_name}, if you mean 'raises the question'? {url}",
    "I don't know @{screen_name}, but I have another issue to raise with you {url}",
    "Raise it, @{screen_name}, don't beg it! 🙌 {url}"
]

def make_it_so():
    client = twitter_client(DEFAULT_CREDS_FILE)
    ################
    # find my most recent reply
    results = client.user_timeline(trim_user = True, exclude_replies = False, include_rts = False, count = 5)
    replies = [r for r in results if r.in_reply_to_status_id]
    if replies:
        # We want to search for tweets that come _after_ the most recent tweet we've replied to...
        xid = replies[0].in_reply_to_status_id
    else:
        xid = 1

    print("Last replied to id is ", xid)

    ##################
    # search for some tweets
    results = client.search(q = '"begs the question why" OR "begging the question why"', since_id = xid,
            result_type = 'recent', count = 100, trim_user = False,
            exclude_replies = True, include_rts = False)
    # trim retweets
    results = [r for r in results if not hasattr(r, 'retweeted_status')]
    # filter out "begging the question[period]"
    results = [r for r in results if 'question.' not in r.text.lower()]

    print("Found %s possible tweets" % len(results))
    if not results:
        return None
    # Just pick the earliest (i.e. last in the list) tweet
    target_tweet = results[-1]

    ######################
    # reply to it
    temptext = POSSIBLE_REPLIES[randrange(0, len(POSSIBLE_REPLIES))]
    url = POSSIBLE_URLS[randrange(0, len(POSSIBLE_URLS))]
    tweet_txt = temptext.format(screen_name = target_tweet.user.screen_name, url = url)
    response = client.update_status(status = tweet_txt, in_reply_to_status_id = target_tweet.id)
    return response



def twitter_client(credsfile):
    ffn = expanduser(credsfile)  # get the full path in case the ~ is used
    c = json.load(open(ffn))
    # Get authentication token
    auth = tweepy.OAuthHandler(consumer_key = c['consumer_key'],
                               consumer_secret = c['consumer_secret'])
    auth.set_access_token(c['access_token'], c['access_token_secret'])
    # create an API handler
    return tweepy.API(auth)



if __name__ == "__main__":
    intervaltime = 800
    loopcount = 0
    maxloopcount = 1000
    print("Hello, going to be raising questions every %s seconds, for at least %s times!" % (intervaltime, maxloopcount))

    while loopcount < maxloopcount:
        loopcount += 1
        print("------------")
        print("On iteration", loopcount)
        resp = make_it_so()
        if resp:
            print("http://twitter.com/_/statuses/%s" % resp.id)
            print("Reply #%s: %s" % (resp.id, resp.text))
            print("to %s" % resp.in_reply_to_screen_name)
        else:
            print("No response from twitter")

        s = intervaltime + randrange(5, 200)
        print("Sleeping for %s seconds" % s)
        sleep(s)
