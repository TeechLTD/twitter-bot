import tweepy

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
            # display_tweet(status)
            print "Listening..... \n"
            act_on_tweet(status)


    def on_error(self, status):
        if status_code is 420:
            return False
        elif status_code is 403:
            return False
        elif status_code is 429:
            return False
        elif status_code is 502:
            sleep(120)
            return False
        elif status_code is 503:
            sleep(120)
            return False
        elif status_code is 504:
            sleep(120)
            return False
        else:
            print(status)
            time.sleep(120)
            return False

def display_tweet(tweet):
    print("Tweet Message : " + tweet.text)
    print("Tweet id : " + str(tweet.id))
    print("Tweet user name : " + tweet.user.name)
    print("Tweet user handle : " + tweet.user.screen_name)
    print("Tweet user id : " + str(tweet.user.id) + "\n")


def act_on_tweet(tweet):
    tweet_id = tweet.id
    user = tweet.user

    follower = follow_us(user)

    try:
        api.create_favorite(tweet_id)
        print("favorited a tweet by: " + user.name)
        print(tweet.text + "\n")
    except Exception as e:
        print("favoriting a tweet by: " + user.name + " failed! \n" )
        print(e)
        print("\n")
        pass

    print("sleeping... " + "\n")
    time.sleep(45)

    if "@aderalv2" in tweet.text:
        try:
            api.retweet(tweet_id)
            reply(tweet_id, user.screen_name)
        except Exception as e:
            print("replying to: " + user.name + " failed!" )
            print(e)
            print "\n"

    if not follower:
        try:
            api.create_friendship(user.id, api.me)
            print("Requested to follow :" + user.name + "\n")
        except Exception as e:
            print("request to follow: " + user.name + " failed!" )
            print(e)
            print "\n"

def reply(tweet_id, user_handle):
    reply = "@%s, we are listening. Join our community today to boost your potential." % (user_handle)
    try:
        api.update_status(reply, tweet_id)
        print("Retweeted and replied to: " + user_handle + "\n")
    except:
        print("reply to: " + user_handle + " failed! \n" )
        pass

def follow_us(user):
    friendship = api.show_friendship(target_id=user.id)
    friends = friendship[1].followed_by
    return friends

def direct_message(user):
    message = "@%s, welcome to our world. To learn more about our exclusive product and reserve your spot in the waitlist - follow the link in our bio." % (user_name)
    try:
        api.send_direct_message(user.id)
        print("sent a direct message to: " + user.name + "\n")
    except:
        print("direct message to: " + user.name + " failed! \n" )
        pass
    time.sleep(90)
