import tweepy, os, time

if os.environ["bot_env"] == 'development':
     from credentials import keys

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        # display_tweet(status)
        act_on_tweet(status)

    def on_error(self, status):
        if status_code == 420:
            return False
        elif status_code == 403:
            return False
        elif status_code == 429:
            return False
        else:
            time.sleep(90)
            return True

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

def unfollow(user_list):
    # TODO
    return None

def listen(stream, search_terms):
    stream.filter(languages=["en"], track=search_terms, async=True)

if __name__ == '__main__':

    os.system('cls||clear')

    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
    auth.secure = True
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5)
    streamListener = StreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=streamListener)

    search_terms = ["adderal", "aderal", "adderral", "I need adderall", '@aderalv2', 'getaderal.com', 'need a tutor', 'A-levels']

    try:
        listen(myStream, search_terms)
    except Exception as e:
        print(e)
        print("\n" + "Restarting stream...." + "\n")
        listen(myStream, search_terms)

print "Listening..... \n"
