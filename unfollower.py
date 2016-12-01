import tweepy, os, time
from credentials import keys

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
    auth.secure = True
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])
    screen_name = 'aderalv2'

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5, timeout=60)

    followers = api.followers_ids(screen_name)
    friends = api.friends_ids(screen_name)

    print("executing in 10 - press ctrl-c to abort")
    count = 0
    
    for f in friends:
        if f not in followers:
            count += 1
            api.destroy_friendship(f)

    print("done - killed " + count + "friendships")
