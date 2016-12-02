import tweepy, time, sys
from credentials import keys

if __name__ == '__main__':
    print "WARNING - Do not execute this script too often: twitter will shut us out of the api if we call on it too many times"

    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
    auth.secure = True
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])
    screen_name = 'aderalv2'

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5, timeout=60)

    try:
        followers = api.followers_ids(screen_name)
        friends = api.friends_ids(screen_name)
    except Exception as e:
        print(e)
        sys.exit

    print ("we are following " + str(len(friends)) + " people")

    upper_bound = int(raw_input("Upper bound on number of friendships to kill ?"))
    count = 0

    print("executing in 10 - press ctrl-c to abort \n")
    time.sleep(10)

    for f in friends[0:upper_bound]:
        count += 1
        if f not in followers:
            #api.destroy_friendship(f)

    print("done - killed " + str(count) + " friendships")
