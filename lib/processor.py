import tweepy
import time

def display_tweet(tweet, api):
    """displays useful information"""

    print("Tweet Message : " + tweet.text)
    print("Tweet id : " + str(tweet.id))
    print("Tweet user name : " + tweet.user.name)
    print("Tweet user handle : " + tweet.user.screen_name)
    print("Tweet user id : " + str(tweet.user.id) + "\n")

def act_on(tweet, api):
    """main logic"""

    user = tweet.user
    follower = follow_us(user, api)
    mention = "@SCREEN_NAME" in tweet.text

    favorite(tweet, api, user)

    time.sleep(45)

    if mention:
        reply_and_retweet(tweet, user, api)

    if not follower:
        follow(user, api)

def favorite(tweet, api, user):
    """tries to favorite a tweet"""
    try:
        api.create_favorite((tweet.id))
        print("favorited a tweet by: " + user.name)
        print(tweet.text + "\n")
    except Exception as e:
        print("favoriting a tweet by: " + user.name + " failed!" )
        print(e)
        print("\n")
    time.sleep(900)

def follow(user, api):
    """follows a specific user"""

    try:
        api.create_friendship(user.id, api.me)
        print("Requested to follow :" + user.name + "\n")
    except Exception as e:
        print("request to follow: " + user.name + " failed!" )
        print(e)
        print "\n"

def reply(tweet, user, api):
    """replies to tweets"""

    reply = "@%s, we are listening. Join our community today to boost your potential." % (user.screen_name)
    try:
        api.retweet(tweet.id)
        api.update_status(reply, tweet.id)
        print("Retweeted and replied to: " + user.screen_name + "\n")
    except:
        print("reply to: " + user.screen_name + " failed!" )
        print(e)

def follow_us(user, api):
    """checks if a user follows us or not"""

    friendship = api.show_friendship(target_id=user.id)
    friends = friendship[1].followed_by
    return friends

def direct_message(user, api):
    """sends a direct message to a user"""

    message = "@%s, welcome to our world. To learn more about our exclusive product and reserve your spot in the waitlist - follow the link in our bio." % (user.screen_name)
    try:
        api.send_direct_message(user.id)
        print("sent a direct message to " + user.name + "\n")
    except:
        print("direct message to: " + user.name + " failed! \n" )

    time.sleep(90)

def direct_message_new_followers(api):
    """runs on stream __init__, messages all new followers"""

    screen_name = ''
    followers = []
    unmessaged_followers = []

    print("Fetching un-messaged followers .... ")
    for user in tweepy.Cursor(api.followers).items():
        followers.append(user)

    for user in followers:
        # check if we messaged the user
        messaged = check_conversation(user, api)
        if not messaged:
            unmessaged_followers.append(user)

    time.sleep(20)
    for user in unmessaged_followers:
        direct_message(user, api)

    print("Messaged un-messaged followers \n")

def check_conversation(user, api):
    # return false if user has not been messaged, true if messaged

    return True
