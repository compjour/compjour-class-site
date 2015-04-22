import foo
import twit_utils
CREDS_FILE = "~/.creds/me.json"

def make_it_so():
    # Step 1. Get my latest tweets
    tweets = twit_utils.get_latest_tweets_from_me(CREDS_FILE)
    print("Found", len(tweets), "tweets")

    # Step 2. From my tweets, get the last time I did a yolobro reply
    breply = foo.latest_yolobro_reply(tweets)
    if breply:
        xid = breply['in_reply_to_status_id']
    else:
        xid = 1
    print("Searching for mentions with an id later than", xid)

    # Step 3. Get the most recent mentions since my last yolobro reply
    mentions = twit_utils.get_mentions(CREDS_FILE, {"since_id": xid})
    print("Found", len(mentions), "mentions")

    # Step 4. from the mentions, see if anyone has used the hashtag #bro
    brotweet = foo.find_first_bro_tagged_mention(mentions)

    if brotweet == None:
        print("No #Bro tweet to reply to")
        return None
    else:
        # Step 5. Create the custom bro message
        print("About to send a message to", brotweet['user']['screen_name'])
        txt = foo.make_yolobro_text()

        # Step 6. Send the message
        resp = twit_utils.reply(CREDS_FILE, txt, brotweet)
        return resp

