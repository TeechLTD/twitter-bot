import sys, os, tweepy, json
from tqdm import tqdm
from time import sleep

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from credentials import keys

def direct_message(target_users):
    """sends a direct message to a list of users"""

    message = "@%s, thanks for following us. As a token of appreciation, get your first session free on our platform. Simply sign up and use the code -- " % (user.screen_name)
    try:
        api.send_direct_message(user.id)
        print("sent a direct message to " + user.name + "\n")
    except:
        print("direct message to: " + user.name + " failed! \n" )

    time.sleep(90)

def get_stored_last_follower():
    last_id = 0

    with open('latest_follower.json') as json_data:
        d = json.load(json_data)
        print(d)

    return

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(keys['TEECH_CONSUMER_KEY'], keys['TEECH_CONSUMER_SECRET'])
    auth.set_TEECH_ACCESS_TOKEN(keys['TEECH_ACCESS_TOKEN'], keys['TEECH_ACCESS_SECRET'])
    screen_name = 'TeechGlobal'

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5, timeout=60)
    screen_name = 'TeechGlobal'

    #fetch all my followers
    # followers =[]
    # for follower in tweepy.Cursor(api.followers_ids, screen_name).items():
    #     followers.append(follower)

    # most_recent_follower = followers[0]


    last_stored_follower_id = get_stored_last_follower()
