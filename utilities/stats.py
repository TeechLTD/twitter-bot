import sys, os, time, tweepy, json
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from credentials import keys

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
    auth.secure = True
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])
    screen_name = 'aderalv2'

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5, timeout=60)

    followers = []
    friends = []

    for follower in tweepy.Cursor(api.followers_ids, screen_name).items():
        followers.append(follower)

    for friend in tweepy.Cursor(api.friends_ids, screen_name).items():
        friends.append(friend)

    data = api.rate_limit_status(ressources=[followers, friends])
    hits_left = data['resources']['followers']['/followers/ids']['remaining']
    hits_left += data['resources']['friends']['/friends/ids']['remaining']

    print(str(hits_left) + " api calls remaining \n")

    print "FOLLOWING - " + str(len(friends)) + " people"
    print "FOLLOWERS - " + str(len(followers)) + " people"
