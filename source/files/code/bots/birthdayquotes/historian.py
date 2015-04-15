from twip import twitter_client

def make_it_so():
    client = twitter_client()
    results = client.user_timeline(trim_user = True, exclude_replies = False, include_rts = True, count = 20)
    replies = [r for r in results if r.in_reply_to_status_id]
    if replies:
        return replies[0].in_reply_to_status_id
    else:
        return None
