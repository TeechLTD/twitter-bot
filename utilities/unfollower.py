import tweepy, sys, os
from tqdm import tqdm
from time import sleep

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from credentials import keys

def fetch_sets():
    followers = []
    friends = []

    for follower in tweepy.Cursor(api.followers_ids, screen_name).items():
        followers.append(follower)

    for friend in tweepy.Cursor(api.friends_ids, screen_name).items():
        friends.append(friend)

    non_reciprocal = list(set(friends) - set(followers))

    return (followers, friends, non_reciprocal)

def unfollow(non_reciprocal, upper_bound):

    # prevent 'out of range errors'
    if upper_bound > len(non_reciprocal):
        upper_bound = len(non_reciprocal)

    subset = reversed([non_reciprocal[i] for i in range(upper_bound)])
    success_count, error_count = 0, 0

    # reverse to start with most ancient
    for f in tqdm(subset, desc="Unfollowing..."):
        try:
            api.destroy_friendship(f)
            success_count += 1
        except Exception as e:
            error = e
            error_count += 1
        sleep(3)

    print("done - killed " + str(success_count) + " non-followers, with " + str(error_count) + " errors")
    if error: print(e)

def fetch_upper_bound():
    upper_bound = int(raw_input("Upper bound on number of friendships to kill ?\nThe bot kills from most ancient to most recent (max 200)\n"))

    if upper_bound > 200:
        upper_bound = 200

    return upper_bound

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])
    screen_name = 'aderalv2'

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5, timeout=60)

    # Create list of followers and people we follow
    followers, friends, non_reciprocal = fetch_sets()

    print "FOLLOWING - " + str(len(friends)) + " people"
    print "FOLLOWERS - " + str(len(followers)) + " people"
    print str(len(non_reciprocal)) + " non-reciprocal followers.\n"

    upper_bound = fetch_upper_bound()

    print("executing in 10 - press ctrl-c to abort - THIS CANNOT BE UNDONE\n")
    sleep(10)

    unfollow(non_reciprocal, upper_bound)
