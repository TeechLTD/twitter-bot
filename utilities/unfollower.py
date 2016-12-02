import tweepy, time, sys
from credentials import keys

if __name__ == '__main__':
    print "WARNING - Do not execute this script too often: twitter will shut us out of the api if we call on it too many times"

    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
    auth.secure = True
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])
    screen_name = 'aderalv2'

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5, timeout=60)

    # Create list of followers and people we follow
    followers = []
    friends = []

    for follower in tweepy.Cursor(api.followers).items():
        followers.append(follower)

    for friend in tweepy.Cursor(api.friends).items():
        friends.append(friend)

    # list of people who do not follow us back
    non_reciprocal = list(set(friends) - set(followers))
    print str(len(non_reciprocal)) + " non-reciprocal followers.\n"

    # fetch api calls status
    data = api.rate_limit_status(ressources=[followers, friends])
    hits_left = data['resources']['followers']['/followers/ids']['remaining']
    hits_left += data['resources']['friends']['/friends/ids']['remaining']

    print(str(hits_left) + " api calls remaining \n")

    upper_bound = int(raw_input("Upper bound on number of friendships to kill ?"))
    count = 0

    print("executing in 10 - press ctrl-c to abort - THIS CANNOT BE UNDONE\n")
    time.sleep(10)

    for f in non_reciprocal[0:upper_bound]:

        if hits_left > 0
            api.destroy_friendship(f)
            count += 1
            hits_left -= 1
        else:
            print("ran out of hits, try later")
            break

    print("done - killed " + str(count) + " friendships")
