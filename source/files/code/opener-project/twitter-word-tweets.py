from twitter_foo import get_ca_tweeters, get_profile, get_tweets_with_word
from datetime import datetime
from jinja2 import Template
the_word = "kenya"


html_file = open("data-hold/word-" + the_word + ".html", "w", encoding = "utf-8")
body_template = Template(
"""
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
   <title>My CA Twitter words</title>
   <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
</head>
<body>
    <section class="container">
        <h1>Congress folks who tweeted about "{{ word }}"</h1>
        <div class="row">
           <div class="col-sm-6">
              <h2>Democrats</h2>
              {{ d_tweets }}
           </div>
           <div class="col-sm-6">
              <h2>Republicans</h2>
              {{ r_tweets }}
           </div>
     </section>
  </body>
  </html>
""")

# Documentation on Twitter's embed tweet code:
# https://dev.twitter.com/web/embedded-tweets
embed_tweet = Template("""
<blockquote class="twitter-tweet" lang="en"><p>
<a href="https://twitter.com/{{screen_name}}/status/{{tweet_id}}">X</a>
</p></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
""")


d_str = ""
r_str = ""

for member in get_ca_tweeters():
    screen_name = member['twitter_id'].lower()
    profile = get_profile(screen_name)
    word_tweets = get_tweets_with_word(screen_name, the_word)
    # if there is at least one tweet with the word
    if len(word_tweets) > 0:
        tweet = word_tweets[0]

        t = embed_tweet.render(screen_name = screen_name, tweet_id = tweet['id'])
        if member['party'] == 'D':
            d_str += t
        else:
            r_str += t



# Now add the d_str and r_str strings, which contain a bunch of HTML, to the main
# body template
html_file.write(body_template.render(word = the_word, d_tweets = d_str, r_tweets = r_str))
html_file.close()
