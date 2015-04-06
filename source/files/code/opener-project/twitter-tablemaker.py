from twitter_foo import get_ca_tweeters, get_profile, get_tweets, get_original_tweets
from twitter_foo import convert_twitter_timestamp, get_tweets_with_word
from datetime import datetime
from jinja2 import Template


html_file = open("data-hold/table.html", "w", encoding = "utf-8")
html_file.write(
"""
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

   <title>My CA Twitter Table</title>
   <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1>Congress folks on Twitter</h1>
        <table class="table table-condensed table-striped">
          <thead>
             <tr>
               <th>Congressmember</th>
               <th>Twitter name</th>
               <th>Party</th>
               <th>Followers</th>
               <th>Tweets</th>
               <th>Days on Twitter</th>
               <th>Daily Twitter Rate</th>
             </tr>
           </thead>
           <tbody>
""")


row_str = """
<tr>
  <td>
    <img src="{{ profile_pic_url }}" style="width: 60px">
    {{ title }} {{ full_name }}
  </td>
  <td>
    <a href="https://twitter.com/{{ twitter_id }}">{{ twitter_id }}</a>
  </td>
  <td>
    {{ party }}
  </td>
  <td>
    {{ followers_count }}
  </td>
  <td>
    {{ tweets_count }}
  </td>
  <td>
    {{ days_ago }}
  </td>
  <td>
    {{ daily_tweet_rate }}
  </td>
</tr>
"""

row_template = Template(row_str)

for member in get_ca_tweeters():
    tid = member['twitter_id'].lower()
    profile = get_profile(tid)
    tweets = get_tweets(tid)

    days_ago = (datetime.today() - convert_twitter_timestamp(profile['created_at'])).days
    tweet_rate = round(profile['statuses_count'] / days_ago, 2)


    data = {
        "profile_pic_url" : profile['profile_image_url'],
        "title" : member['title'],
        "party" : member['party'],
        "full_name" : " ".join([member['firstname'], member['lastname']]),
        "twitter_id": tid,
        "followers_count":  profile['followers_count'],
        "tweets_count": profile['statuses_count'],
        "days_ago": days_ago,
        "daily_tweet_rate": tweet_rate
        }
    html_file.write(row_template.render(data))


html_file.write("</table></div>")
html_file.close()
