from twip import twitter_client
import re
from random import randrange

TEMPLATETWEETS = [
'via {speaker}: "{quote}"',
'"{quote}" - {speaker}',
'Always remember: "{quote}" - {speaker}',
'{speaker} once said: "{quote}"'
]

def make_it_so(tweets):
    d =  make_a_quote()
    d['template'] = TEMPLATETWEETS[randrange(0, len(TEMPLATETWEETS))]
    # now let's find a birthday person
    if tweets:
        t = tweets[randrange(0, len(tweets))]
        bstr = 'Happy birthday @%s!' % t.user.screen_name
        d['template'] =  bstr + ' ' + d['template']
        d['reply_to_status_id'] = t.id

    return d


def make_a_quote():
    quotes = []
    speakers = []
    tweets = twitter_client().user_timeline('greatestquotes', count = 200, trim_user = True)
    for t in tweets:
        m = re.search('"(.+?)" - (.+)', t.text)
        if m:
            q, s = m.groups()
            quotes.append(q)
            speakers.append(s)

    d = {}
    d['quote'] = quotes[randrange(0, len(quotes))]
    d['speaker'] = speakers[randrange(0, len(speakers))]

    return d
