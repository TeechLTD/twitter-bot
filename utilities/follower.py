import sys, os, tweepy
from tqdm import tqdm
from time import sleep

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from credentials import keys

def get_parameters():
    """Left as a method to allow for multiple account selecting in the future"""

    target_account = raw_input("Enter an account's twitter handle \n")
    upper_bound = int(raw_input("Enter an upper bound on the total number of people you wish to follow - \n"))

    return (target_account, upper_bound)

def follow(users):

    success_count = 0
    error_count = 0

    for user_id in tqdm(target_users, desc="sending follow requests", leave=False):
        try:
            api.create_friendship(user_id, api.me)
            success_count += 1
            sleep(1)
        except Exception as e:
            error_count += 1

    print("\n followed " + str(success_count) + " user(s), with " + str(error_count) + " error(s)")

def fetch_users(target_account, upper_bound):
    target_users = []

    for follower in tweepy.Cursor(api.followers_ids, target_account).items(upper_bound):
        target_users.append(follower)

    return target_users

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
    auth.secure = True
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])
    screen_name = 'aderalv2'

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5, timeout=60)

    target_account, upper_bound = get_parameters()

    target_users = fetch_users(target_account, upper_bound)
    print("Loaded " + str(len(target_users)) + " users into the pipeline \n")
    sleep(1)

    follow(target_users)
