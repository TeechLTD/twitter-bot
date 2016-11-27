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
    print("Tweet id : " + tweet.id.encode('utf-8'))
    print("Tweet user : " + tweet.user.name)
    print("Tweet user id : " + (tweet.user.id).encode('utf-8') + "\n")


def act_on_tweet(tweet):
    tweet_id = tweet.id
    user = tweet.user

    follower = follow_us(user)
    time.sleep(90)

    try:
        api.create_favorite(tweet_id)
        print("favorited a tweet by: " + user.name)
        print(tweet.text + "\n")
    except Exception as e:
        print("favoriting a tweet by: " + user.name + " failed! \n" )
        print(e)
        print("\n")
        pass

    time.sleep(90)

    if "@aderalv2" in tweet.text:
        try:
            api.retweet(tweet_id)
            reply(tweet_id, user.name)
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

    time.sleep(90)

def reply(tweet_id, user_name):
    reply = "@%s, we are listening. Join our community today to boost your potential." % (user_name)
    try:
        api.update_status(reply, tweet_id)
        print("Retweeted and replied to: " + user.name + "\n")
        time.sleep(90)
    except:
        print("reply to: " + user.name + " failed! \n" )
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


if __name__ == '__main__':

    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
    auth.secure = True
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5)
    streamListener = StreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=streamListener)

    search_terms = ["adderal", "aderal", "adderral", "I need adderall", '@aderalv2', 'getaderal.com', 'need a tutor', 'A-levels']
    myStream.filter(languages=["en"], track=search_terms, async=True)

print "Listening..... \n"
