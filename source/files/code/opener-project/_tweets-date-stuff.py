



latest_tweet_time = datetime.strptime(tweets[0]['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
oldest_tweet_time = datetime.strptime(tweets[-1]['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
diff_time = (latest_tweet_time - oldest_tweet_time).days
recent_daily_tweet_rate = round(len(tweets) / diff_time, 2)
print("In the last {} tweets, the tweet rate is {} tweets/day".format(len(tweets), recent_daily_tweet_rate))


# Get tweets that are not retweets
original_tweets = [t for t in tweets if t.get('retweeted_status') == None]
print("Has {} original tweets in his last {}".format(len(original_tweets), len(tweets)))
# Get most retweeted Tweet
tweets_sorted_by_rts = sorted(original_tweets, key = itemgetter('retweet_count'), reverse = True)
rt = tweets_sorted_by_rts[0]
print("Most retweeted tweet has {} RTs and said: {}".format(rt['retweet_count'], rt['text']))

tweets_by_hour = [0] * 24
for t in tweets:
    tdate = datetime.strptime(t['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
    d = tdate + timedelta(hours = -4) # EST is -4 hours from GMT
    tweets_by_hour[d.hour] += 1


for idx, tweet_count in enumerate(tweets_by_hour):
