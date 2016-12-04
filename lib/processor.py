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
    mention = "@TeechGlobal" in tweet.text

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

    reply = "@%s, We can help! " % (user.screen_name)
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
