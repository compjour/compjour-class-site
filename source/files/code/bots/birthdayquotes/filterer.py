from datetime import date

def make_it_so(tweets):
    ftweets = []
    # remove tweets that are actually retweets
    for t in tweets:
        if hasattr(t, 'retweeted_status') is False and t.created_at.date() == date.today():
            ftweets.append(t)

    return ftweets
