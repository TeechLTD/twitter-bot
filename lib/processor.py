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
    needs_a_tutor = "I need a tutor" in tweet.text

    favorite(tweet, api, user)

    if not follower:
        follow(user, api)

    if needs_a_tutor:
        reply = "@%s, we can connect you with a tutor for a video chat within minutes! First session is on us. DM for details" %(user.screen_name)
        reply(tweet, user, reply, api)

    # Commented out for now
    # if mention:
    #     reply = "@%s, thanks for reaching out! DM us your question and we'll take care o" % (user.screen_name)
    #     reply(tweet, user, reply, api)

    time.sleep(90)

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
    time.sleep(90)

def follow(user, api):
    """follows a specific user"""

    try:
        api.create_friendship(user.id, api.me)
        print("Requested to follow :" + user.name + "\n")
    except Exception as e:
        print("request to follow: " + user.name + " failed!" )
        print(e)
        print "\n"

def reply(tweet, user, reply, api):
    """replies to tweets"""

    try:
        api.retweet(tweet.id)
        api.update_status(reply, tweet.id)
        print("Retweeted and replied to: " + user.screen_name + "\n")
        print("Original tweet - " + tweet.text + "\n")
    except:
        print("reply to: " + user.screen_name + " failed!" )
        print(e)

    time.sleep(90)

def follow_us(user, api):
    """checks if a user follows us or not"""

    friendship = api.show_friendship(target_id=user.id)
    friends = friendship[1].followed_by
    return friends

def direct_message(user, api):
    """sends a direct message to a user"""

    message = "@%s, thanks for the follow. To show you our appreciation - your first class will be free on the app. Take a picture of your problem and send it to our network of profs. Most are top class upper-years or Phd's from Oxford, Cambridge and other leading universities with excellent knowledge of their topic. They answer in under 30 seconds on average. - Reach out to us with any questions - we're only a DM away. Love, Teech team" % (user.screen_name)
    try:
        api.send_direct_message(user.id)
        print("sent a direct message to " + user.name + "\n")
    except:
        print("direct message to: " + user.name + " failed! \n" )

    time.sleep(90)
