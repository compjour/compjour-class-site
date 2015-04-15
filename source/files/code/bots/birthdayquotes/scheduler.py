import historian, collector, decider, filterer, sender
from random import randrange
from time import sleep

def make_it_so():
    xid = historian.make_it_so()
    print('Last tweet ID:', xid)

    tweets = collector.make_it_so(xid)
    print('Tweets collected:', len(tweets))

    ftweets = filterer.make_it_so(tweets)
    print('Filtered tweets:', len(ftweets))

    obj = decider.make_it_so(ftweets)
    print('The tweet template:', obj)

    resp = sender.make_it_so(obj)
    if resp:
        print("Tweet was sent:", resp.id)
        print(resp.text)
        print("https://twitter.com/_/statuses/" + str(resp.id))




if __name__ == "__main__":
    intervaltime = 300
    loopcount = 0
    maxloopcount = 1000
    print("Hello, going to be raising questions every %s seconds, for at least %s times!" % (intervaltime, maxloopcount))

    while loopcount < maxloopcount:
        loopcount += 1
        print("------------")
        print("On iteration", loopcount)
        resp = make_it_so()

        s = intervaltime + randrange(5, 200)
        print("Sleeping for %s seconds" % s)
        sleep(s)
