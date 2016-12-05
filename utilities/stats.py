import sys, os, time, tweepy, json
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from credentials import keys

def fetch_api_status():
    data = api.rate_limit_status()
    hits_left = data['resources']['followers']['/followers/ids']['remaining']
    hits_left += data['resources']['friends']['/friends/ids']['remaining']

    return hits_left

def fetch_sets():
    followers = []
    friends = []

    for follower in tweepy.Cursor(api.followers_ids, screen_name).items():
        followers.append(follower)

    for friend in tweepy.Cursor(api.friends_ids, screen_name).items():
        friends.append(friend)

    non_reciprocal = list(set(friends) - set(followers))

    return (followers, friends, non_reciprocal)


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(keys['TEECH_CONSUMER_KEY'], keys['TEECH_CONSUMER_SECRET'])
    auth.set_TEECH_ACCESS_TOKEN(keys['TEECH_ACCESS_TOKEN'], keys['TEECH_ACCESS_SECRET'])
    screen_name = 'TeechGlobal'

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5, timeout=60)

    followers, friends, non_reciprocal = fetch_sets()
    hits_left = fetch_api_status()

    print(str(hits_left) + " api calls remaining \n")
    print "FOLLOWING - " + str(len(friends)) + " people"
    print "FOLLOWERS - " + str(len(followers)) + " people"
    print str(len(non_reciprocal)) + " non-reciprocal followers.\n"
