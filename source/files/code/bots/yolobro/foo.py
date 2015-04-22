from random import random

def find_first_bro_tagged_mention(mentions):
    """
    Given a list of tweets (ostensibly from the mentions-API-endpoint),
    find the earliest one that has the #BRO hashtag in it

    Arguments:
        mentions (list): a list of Twitter tweet objects that are dicts

    Returns:
        if any such tweet is found, return that tweet (dict)
        else, return None
    """
    bmentions = []
    for m in mentions:
        hashtags = m['entities']['hashtags']
        for tag in hashtags:
            if tag['text'].upper() == "BRO":
                bmentions.append(m)

    if len(bmentions) > 0:
        return bmentions[0]
    else:
        return None



def latest_yolobro_reply(tweets):
    """
    Given a list of tweets (ostensibly from user_timeline API endpoint),
    find the earliest one that has the #YOLOBRO hashtag in it

    Arguments:
        tweets (list): a list of Twitter tweet objects that are dicts

    Returns:
        if any such tweet is found, return that tweet (dict)
        else, return None
    """
    for tweet in tweets:
        tags = [tag for tag in tweet['entities']['hashtags'] if tag['text'].upper() == 'YOLOBRO']
        if len(tags) > 0:
            return tweet


def make_yolobro_text():
"""
    Create a custom #YOLOBRO happy message
    Arguments:
        None
    Returns:
        A text string with the #YOLOBRO hashtag and something extra special
    """
    if random() > 0.7:
        return "#YOLOBRO YOU MY BRO!"
    else:
        return "#YOLOBRO YO YO"
