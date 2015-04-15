from twip import twitter_client
LIST_OWNER_SCREEN_NAME = 'mashable'
LIST_SLUG = 'news'

def make_it_so(sid = 1):
    client = twitter_client()
    tweets = client.list_timeline(owner_screen_name = LIST_OWNER_SCREEN_NAME,
                                    slug = LIST_SLUG, since_id = sid, count = 100,
                                    trim_user = False,  include_rts = False)

    return tweets

