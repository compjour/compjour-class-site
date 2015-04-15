from twip import twitter_client
QUERY_STR = '"today is my birthday"'


def make_it_so(sinceid = 1):
    sinceid = 1 #TKTK
    client = twitter_client()
    results = client.search(q = QUERY_STR, since_id = sinceid, result_type = 'recent', count = 200,
            trim_user = False,  exclude_replies = True, include_rts = False)
    return results

