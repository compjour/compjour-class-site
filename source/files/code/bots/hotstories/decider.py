import math

def make_it_so(tweets):
    # get the top 5 tweets according to fleek score
    return sorted(tweets, key = fleekness, reverse = True)[0]


# given a tweet
# returns a number that is purportedly an index of how great the tweet is
def fleekness(tweet):
    fleek_score = tweet.retweet_count
    fleek_score += tweet.favorite_count * 0.2
    fleek_score += math.log(tweet.user.followers_count)

    return fleek_score

