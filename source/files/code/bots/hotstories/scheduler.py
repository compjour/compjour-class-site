import collector, decider, sender
from time import sleep

def make_it_so(starting_tweet_id = None):
    # Collect some tweets
    tweets = collector.make_it_so(starting_tweet_id)
    print('Tweets collected:', len(tweets))
    # Decide which tweet to retweet
    the_tweet = decider.make_it_so(tweets)
    # Retweet that tweet
    resp = sender.make_it_so(the_tweet)
    # return the Twitter response
    if resp:
        print("Tweet was sent:", resp.id)
        print(resp.text)
        print("https://twitter.com/_/statuses/" + str(resp.id))
        return resp




if __name__ == "__main__":
    intervaltime = 600
    starting_tweet_id = None
    print("Hello, going to be retweeting fleekness every %s seconds" % intervaltime)

    while True:
        print("------------")
        resp = make_it_so(starting_tweet_id)

        sleep(intervaltime)
