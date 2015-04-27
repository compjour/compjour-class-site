import profile_tests
import followers_tests
import tweets_tests
import twit_utils


screen_name = 'nytimes'
userdict = twit_utils.get_user(screen_name)

profilescore = profile_tests.score(userdict['profile'])
tweetsscore = tweets_tests.score(userdict['tweets'])
followersscore = followers_tests.score(userdict['followers'])

print("%s got %s points for profile" % (screen_name, profilescore))
print("%s got %s points for tweets" % (screen_name, tweetsscore))
print("%s got %s points for followers" % (screen_name, followersscore) )
print("Total:", sum([profilescore, tweetsscore, followersscore]))
