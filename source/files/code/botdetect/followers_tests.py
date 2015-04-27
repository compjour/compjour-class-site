def score(followers):
    foo_list = [test_overall_follower_friend_ratio]
    total = 0
    for f in foo_list:
        total += f(followers)

    return total



def test_overall_follower_friend_ratio(followers):
    """
    this is basically a copy of the profile_tests version...which means
    we should find a way to reuse that instead of repeating this...
    """

    followers_ct = 0
    friends_ct = 0
    for user in followers:
        followers_ct += user['followers_count']
        friends_ct += user['friends_count']

    ratio = followers_ct / friends_ct
    if ratio > 10:
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
