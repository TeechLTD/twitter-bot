import sys, os, tweepy
from tqdm import tqdm
from time import sleep

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from credentials import keys

def get_parameters():
    """Left as a method to allow for multiple account selecting in the future"""

    target_account = raw_input("Enter an account's twitter handle \n")
    upper_bound = int(raw_input("Enter an upper bound on the total number of people you wish to follow (max 190)- \n"))

    if upper_bound > 190:
        upper_bound = 190

    return (target_account, upper_bound)

def follow(users):

    success_count, error_count = 0, 0
    for user_id in tqdm(target_users, desc="sending follow requests"):
            try:
                api.create_friendship(user_id, api.me)
                success_count += 1
                sleep(3)
            except Exception as e:
                error_count += 1

    print("\nFollowed " + str(success_count) + " user(s), with " + str(error_count) + " error(s)")

def fetch_users(target_account, upper_bound):
    target_users = []
    friends = []

    for friend in tweepy.Cursor(api.friends_ids, screen_name).items():
        friends.append(friend)

    for follower in tweepy.Cursor(api.followers_ids, target_account).items(upper_bound):
        #look for follower upper_bound + 1 if we already follow current one
        if follower in friends:
            upper_bound += 1
        else:
            target_users.append(follower)

    return target_users


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])
    screen_name = 'TeechGlobal'

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5, timeout=60)

    target_account, upper_bound = get_parameters()

    target_users = fetch_users(target_account, upper_bound)

    if len(target_users) is 0:
        print("We already follow all their followers")
        sys.exit()

    print("Loaded " + str(len(target_users)) + " users into the pipeline \n")
    sleep(3)

    follow(target_users)
