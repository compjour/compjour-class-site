
def score(tweets):
    foo_list = [test_hashtags_per_tweet, test_short_tweets, test_links_per_tweets, test_variety_of_mentions]
    total = 0
    for f in foo_list:
        total += f(tweets)

    return total


def test_hashtags_per_tweet(tweets):
    tagcount = sum( [len(t['entities']['hashtags']) for t in tweets]  )
    if tagcount / len(tweets) > 1.5:
        return -1
    else:
        return 0


def test_short_tweets(tweets):
    short_tweets = [t for t in tweets if len(t['text']) < 12]
    ratio = len(short_tweets) / len(tweets)
    if ratio > 0.4:
        return -2
    elif ratio > 0.2:
        return -1
    else:
        return 0

def test_links_per_tweets(tweets):
    urlscount = sum( [len(t['entities']['hashtags']) for t in tweets]  )
    if urlscount / len(tweets) > 1.1:
        return -1
    else:
        return 0


def test_variety_of_mentions(tweets):
    """
    if user is just mentioning names all over the place, could be a sign
    that it has few actual friends, and is just trying to get attention
    """
    mentioned = []
    for t in tweets:
        for u in t['entities']['user_mentions']:
            mentioned.append(u['id'])

    if len(mentioned) < 10:
        return 0
    elif len(mentioned) / len(set(mentioned)) > 0.9:
        return -1
    else:
        return -1
