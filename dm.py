##NOT WORKING YET

import tweepy, os, time
from credentials import keys

def direct_message_new_followers():
    # REMEMBER - takes an api instance
    """runs on stream __init__, messages all new followers"""

    screen_name = 'aderalv2'
    followers = []
    unmessaged_followers = []

    print("Fetching un-messaged followers .... ")
    for user in tweepy.Cursor(api.followers).items():
        followers.append(user)

    api.sent_direct_messages((api.me, 1))

    #
    # #create list of unmessaged followers
    #
    # for user in unmessaged_followers:
    #     # direct_message(user, api)
    #
    # print("Messaged un-messaged followers \n")

def check_conversation():
    # return false if user has not been messaged, true if messaged
    return True

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
    auth.secure = True
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5, timeout=60)

    print("still in development")

    # direct_message_new_followers()
