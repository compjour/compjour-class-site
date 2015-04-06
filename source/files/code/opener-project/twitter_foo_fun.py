from twitter_foo import get_ca_tweeters, get_profile, get_tweets, get_original_tweets
from twitter_foo import convert_twitter_timestamp, get_tweets_with_word
from datetime import datetime

ca_tweeters = get_ca_tweeters()
print("There are {} CA tweeters".format(len(ca_tweeters)))

for member in ca_tweeters:
    tid = member['twitter_id'].lower()
    profile = get_profile(tid)
    tweets = get_tweets(tid)

    days_ago = (datetime.today() - convert_twitter_timestamp(profile['created_at'])).days
    tweet_rate = round(profile['statuses_count'] / days_ago, 2)

    print("----------------")
    istr = "{} has {} followers and tweets {} times per day since joining Twitter {} days ago"
    print(istr.format(tid, profile['followers_count'], tweet_rate, days_ago))
    wrd = 'obama'
    wrd_tweets = get_tweets_with_word(tid, wrd)
    print("Number of original tweets with '{}' in last 200 tweets: {}".format(
                                            wrd, len(wrd_tweets)))

