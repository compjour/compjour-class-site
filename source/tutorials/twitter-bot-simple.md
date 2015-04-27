---
title: "Simple Metrics for Detecting Twitter Bots"
---


First, create a sub-directory (anywhere on your system, even your `tmp` directory).


Then create a file named `twit_utils.py` and copy the code below. Make sure to have `DEFAULT_TWITTER_CREDS_PATH` point to whereever _you_ have a creds file (which you should have gotten from this lesson: <%= link_to_slug 'twitter-app-authentication-process' %>)

<%= codepiece 'botdetect/twit_utils.py' %>


In your Terminal, go to that directory where you saved `twit_utils.py` to, and get into __iPython__.

Once in iPython, you should be able to do this:

~~~py
import twit_utils.py

userdict = twit_utils.get_user("stanford")
# calculate followers-to-friends(i.e. others-followed) ratio:
print(userdata['profile']['followers_count'] / userdata['profile']['friends_count'] )
~~~

If you're having trouble getting that data through Twitter, you can download it from my cached version:


~~~py
import requests
users = {}
baseurl = "http://stash.compjour.org/data/twitter/botdetect/"
snames = ['shaq', 'stanford', 'taylorswift13']
for name in snames:
    users[name] = requests.get(baseurl + name + '.json').json()


~~~



Some sample methods for testing the authenticity of the profile (see [example JSON here](https://dev.twitter.com/rest/reference/get/users/show)):

<%= codepiece 'botdetect/profile_tests.py' %>

Hillary Clinton's [social media account bore some scrutiny](http://www.breitbart.com/big-government/2015/04/15/hillary-clinton-big-on-social-media-especially-with-people-who-dont-exist/) (as did [Sen. John McCain before her, and many others](http://thehill.com/blogs/twitter-room/other-news/244985-study-congressional-twitter-accounts-plagued-by-fake-followers)).

Take [a look at her followers page (currently listing 3.4M+ users)](https://twitter.com/HillaryClinton/followers). Glance across some of the profiles. Then check a more-controlled/curated list of Twitter users: the several hundred users that Twitter-celeb [Ashton Kutcher has _chosen_ to follow](https://twitter.com/aplusk/following).


