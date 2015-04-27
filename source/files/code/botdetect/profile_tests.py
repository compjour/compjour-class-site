import re
import time
from datetime import datetime
from twit_utils import convert_twitter_timestamp

def score(profile):
    foo_list = [test_days_old, test_followers_per_day, test_follower_friend_ratio, test_verification, test_numbers_in_name, test_uncommon_letters_in_screenname]
    total = 0
    for f in foo_list:
        total += f(profile)

    return total



def account_age_in_days(profile):
    xd = convert_twitter_timestamp(profile['created_at'])
    days_old = (datetime.now() - xd).days
    return days_old


def test_days_old(profile):
    if account_age_in_days(profile) < 21:
        return -2
    else:
        return 0


def test_followers_per_day(profile):
    followers_per_day = profile['followers_count'] / account_age_in_days(profile)

    if followers_per_day > 10:
        return 2
    elif followers_per_day > 2:
        return 1
    else:
        return 0


def test_follower_friend_ratio(profile):
    ratio = profile['followers_count'] / profile['friends_count']
    if profile['followers_count'] < 10:
        return 0
    elif ratio > 10:
        return 3
    elif ratio > 3:
        return 2
    elif ratio > 1.01:
        return 1
    elif ratio < 0.6:
        return -1
    elif ratio < 0.1:
        return -2
    else:
        return 0


def test_verification(profile):
    if(profile['verified'] == True):
        return 10
    else:
        return 0

def test_listed_ratio(profile):
    if(profile['followers_count'] > 500):
        if(profile['listed_count'] > 1):
            return 1
        else:
            return -1

    return 0


def test_numbers_in_name(profile):
    matches = re.findall('\d', profile['screen_name'])
    if len(matches) > 4:
        return -2
    elif len(matches) >= 3:
        return -1
    else:
        return 0


def test_uncommon_letters_in_screenname(profile):
    matches = re.findall('xzqyv', profile['screen_name'])
    if len(matches) > 5:
        return -1
    else:
        return 0
