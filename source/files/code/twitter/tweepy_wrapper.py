# The currently serving U.S. congressmember with the most Twitter followers
import json
import os
import tweepy
from datetime import datetime
from jinja2 import Template
DEFAULT_TWITTER_CREDS_PATH = '~/.twittercreds.json'

def get_twitter_client(path = DEFAULT_TWITTER_CREDS_PATH):
    """
    returns: a Tweepy API object
    """
    full_creds_path = os.path.expanduser(path)
    creds = json.load(open(full_creds_path))
    auth = tweepy.OAuthHandler(consumer_key = creds['consumer_key'],
        consumer_secret = creds['consumer_secret'])
    auth.set_access_token(creds['access_token'],
      creds['access_token_secret'])
    return tweepy.API(auth)

# gets a whole bunch of tweets
def get_full_user_timeline(screen_name, api = None, count = 3300):
    if api is None:
        api = get_twitter_client()
    tweets = []
    cursor = tweepy.Cursor(api.user_timeline, id = screen_name,
      trim_user = True, exclude_replies = False, include_rts = True)
    for tweet in cursor.items(count):
        tweets.append(tweet._json)

    return tweets


# returns a list of screen_names found in the tweets that were actual replies
def get_screen_names_replied_to(tweets_arr, api = None):
    tweets = tweepy_to_dict(tweets_arr)
    if api is None:
        api = get_twitter_client()

    screen_names = set()
    for t in tweets:
        if t['in_reply_to_screen_name']:
            screen_names.add(t['in_reply_to_screen_name'].lower())
    # now fetch the
    return screen_names






# https://dev.twitter.com/rest/reference/get/lists/members
def get_all_list_members(list_owner, list_slug, api = None):
    if api is None:
        api = get_twitter_client()
    members = []
    cursor = tweepy.Cursor(api.list_members, count = 5000,
        owner_screen_name = list_owner, slug = list_slug)
    for m in cursor.items():
        members.append(m._json)

    return members

############

def create_members_web_table(arr):
    members = tweepy_to_dict(arr)
    content = """
    <table class="table tablesorter table-condensed table-striped">
    <thead><tr>
    <th>Name</th>
    <th>Bio</th>
    <th>Last tweet</th>
    <th>Days since last tweet</th>
    <th>Twitter client</th>
    <th>Tweets</th>
    <th>Followers</th>
    <th>Friends</th>
    <th>Days since joined</th>
    <th>Tweets per day</th>
    </tr></thead>
    <tbody>
    """

    html_rows = []
    for m in members:
        days_since_joined = days_since_ts(m['created_at'])
        if m['friends_count'] > 0:
            followers_ratio = round(m['followers_count'] / m['friends_count'])
        else:
            followers_ratio = m['followers_count']

        t = m.get('status')
        if t:
            latest_tweet_text = t['text']
            days_since_latest_tweet = days_since_ts(t['created_at'])
            twitter_source = re.search('>(.+?)<', t['source']).groups()[0]

        else:
            latest_tweet_text = ""
            twitter_source = ""
            days_since_latest_tweet = days_since_joined

        mstr = TWEET_HTML.render(
            name = m['name'],
            screen_name = m['screen_name'],
            profile_pic = m['profile_image_url'],
            bio = m['description'],
            followers_count = m['followers_count'],
            friends_count = m['friends_count'],
            days_since_joined = days_since_joined,
            tweets_count = m['statuses_count'],
            tweets_per_day = round(m['statuses_count'] / days_since_joined, 1),
            latest_tweet_text = latest_tweet_text,
            days_since_latest_tweet = days_since_latest_tweet,
            twitter_source = twitter_source
        )
        html_rows.append(mstr)

    content += "\n".join(html_rows)
    content += "</tbody></body></html>"

    return PAGE_HTML.render(content = content)






def convert_twitter_timestamp(ts):
    # ts looks like: "Fri Oct 03 20:18:31 +0000 2008"
    return datetime.strptime(ts, '%a %b %d %H:%M:%S +0000 %Y')

# ts looks like: "Fri Oct 03 20:18:31 +0000 2008"
def days_since_ts(ts):
    t = convert_twitter_timestamp(ts)
    return (datetime.today() - t).days


# A convenience function for converting Tweepy models into plain
# ol lists and dicts
def tweepy_to_dict(collection):
    if collection is dict:
        return collection
    else:
        arr = []
        for i in collection:
            arr.append(i._json)
    return arr




PAGE_HTML = Template(
"""
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

   <title>Some Page</title>
   <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
   <link rel="stylesheet" href="http://stash.compjour.org/assets/css/tablesorter/theme.blue.css">
   <script src="https://code.jquery.com/jquery-1.11.2.min.js"></script>

   <script src="http://stash.compjour.org/assets/js/jquery.tablesorter.combined.js"></script>

   <script>
    $(function() {
       $('.tablesorter').tablesorter({theme: 'blue'});
    });
   </script>


</head>
<body>
    <div class="container">
      {{ content}}
    </div>
</body>
</html>
"""
)


TWEET_HTML = Template(
"""
<tr>
    <td class="name">
        <img src="{{profile_pic}}">
        <br>
        {{ name }}<br>
        <a href="https://twitter.com/{{ screen_name}}">
            @{{ screen_name}}
        </a>
    </td>
    <td class="bio">{{ bio }}</td>
    <td class="tweet">{{ latest_tweet_text }}</td>
    <td class="num">{{ days_since_latest_tweet }}</td>
    <td>{{twitter_source}}</td>
    <td class="num">{{ tweets_count }}</td>
    <td class="num">{{ followers_count }}</td>
    <td class="num">{{ friends_count }}</td>
    <td class="num">{{ days_since_joined }}</td>
    <td class="num">{{ tweets_per_day }}</td>
</tr>
"""
)
