def display_tweet(tweet):
    """displays useful information"""

    print("Tweet Message : " + tweet.text)
    print("Tweet id : " + str(tweet.id))
    print("Tweet user name : " + tweet.user.name)
    print("Tweet user handle : " + tweet.user.screen_name)
    print("Tweet user id : " + str(tweet.user.id) + "\n")

def act_on(tweet, api):
    """main logic"""

    tweet_id = tweet.id
    user = tweet.user
    follower = follow_us(user)
    mention = "@aderalv2" in tweet.text

    favorite(tweet)

    print("sleeping... " + "\n")
    time.sleep(45)

    if mention:
        reply_and_retweet(tweet_id, user.screen_name)

    if not follower:
        follow(user.id, api.me)

def favorite(tweet_id):
    """tries to favorite a tweet"""

    print("3")
    try:
        api.create_favorite(tweet_id)
        print("favorited a tweet by: " + user.name)
        print(tweet.text + "\n")
    except Exception as e:
        print("favoriting a tweet by: " + user.name + " failed! \n" )
        print(e)
        print("\n")
        pass

def follow(user_id, bot):
    try:
        api.create_friendship(user_id, bot)
        print("Requested to follow :" + user.name + "\n")
    except Exception as e:
        print("request to follow: " + user.name + " failed!" )
        print(e)
        print "\n"

def reply(tweet_id, user_handle):
    """replies to tweets"""

    reply = "@%s, we are listening. Join our community today to boost your potential." % (user_handle)
    try:
        api.retweet(tweet_id)
        api.update_status(reply, tweet_id)
        print("Retweeted and replied to: " + user_handle + "\n")
    except:
        print("reply to: " + user_handle + " failed! \n" )
        pass

def follow_us(user):
    """checks if a user follows us or not"""

    friendship = api.show_friendship(target_id=user.id)
    friends = friendship[1].followed_by
    return friends

def direct_message(user):
    """sends a direct message to a user"""

    message = "@%s, welcome to our world. To learn more about our exclusive product and reserve your spot in the waitlist - follow the link in our bio." % (user_name)
    try:
        api.send_direct_message(user.id)
        print("sent a direct message to: " + user.name + "\n")
    except:
        print("direct message to: " + user.name + " failed! \n" )
        pass
    time.sleep(90)
