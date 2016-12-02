import sys, os, time, tweepy
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from credentials import keys

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
    auth.secure = True
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])
    screen_name = 'aderalv2'

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5, timeout=60)

    target_accounts = ['']
    target_followers = []

    for account in target_accounts:
        for follower in tweepy.Cursor(api.followers_ids, account).items(20):
            target_followers.append(follower)

    print("Loaded " + str(len(target_followers)) + " followers into the pipeline")
    time.sleep(10)

    count = 0
    print("Starting.. this might take a while \n")
    for user_id in target_followers:
        try:
            api.create_friendship(user_id, api.me)
            count += 1
            time.sleep(2)
        except Exception as e:
            print(e)
            print "\n"

    print("Followed " + str(count) + "people")
