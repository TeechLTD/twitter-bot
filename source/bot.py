import tweepy, os, time
from tweets import replies, message

if os.environ["bot_env"] == 'development':
     from credentials import keys

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        display_tweet(status)
        act_on_tweet(status)

    def on_error(self, status):
        if status_code == 420:
            return False
        elif status_code == 403:
            return False
        elif status_code == 429:
            return False
        else:
            time.sleep(15)
            return True

def display_tweet(tweet):
    print("Tweet Message : " + tweet.text)
    print("Tweet id : " + str(tweet.id))
    print("Tweet user : " + tweet.user.name)
    print("Tweet user id : " + str(tweet.user.id) + "\n")

def act_on_tweet(tweet):
    tweet_id = tweet.id
    user_id = tweet.user.id
    user_name = tweet.user.name

    # favorite tweet
    bot.create_favorite(tweet_id)

    if "getaderalv2" in tweet.text
    reply = "@%s, you've been invited to join our community.We are revolutionizing the market. getaderal.com" % (user_name)
    try:
        bot.update_status(reply, tweet_id)
        wait_a_minute
    except:
        pass

    wait_a_minute

def direct_message(user):

    try:
        bot.send_direct_message


def unfollow(user_list):

    return None

# prevent excessive spamming
def wait_a_minute():
    sleep(60)

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
    auth.secure = True
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])

    # create bot
    bot = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5)

    # Create stream
    streamListener  = StreamListener()
    myStream = tweepy.Stream(auth=bot.auth, listener=streamListener)

    search_terms = ["adderal", "aderal", "adderral", "I need adderall", '@getaderalv2', 'getaderal.com']
    myStream.filter(languages=["en"], track=search_terms, async=True)



print "Fetching..... \n"
