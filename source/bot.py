import tweepy, os, time
from tweets import replies, message

if os.environ["bot_env"] == 'development':
     from credentials import keys

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        get_tweet(status)
        act_on_tweet(status)

    def on_error(self, status):
        print status
        time.sleep(15)
        return True

def get_tweet(tweet):
    print("Tweet Message : " + tweet.text + "\n")

def act_on_tweet(tweet):

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
    auth.secure = True
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])

    bot = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5)

    streamListener  = StreamListener()
    myStream = tweepy.Stream(auth=bot.auth, listener=streamListener)

    search_terms = ["adderal", "aderal", "adderral", "I need adderall", "Education", "need a tutor"]
    myStream.filter(track=search_terms, async=True)

print "Fetching..... \n"
