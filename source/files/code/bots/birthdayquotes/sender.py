from twip import twitter_client



def make_it_so(obj):
    txt = obj['template'].format(quote = obj['quote'], speaker = obj['speaker'])
    r = twitter_client().update_status(status = txt)

    return r

